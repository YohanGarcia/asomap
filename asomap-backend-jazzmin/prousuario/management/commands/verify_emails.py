from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from prousuario.models import ClaimRequest
from prousuario.utils import verify_email_sent, get_email_status


class Command(BaseCommand):
    help = 'Verifica el estado de emails enviados para reclamos'

    def add_arguments(self, parser):
        parser.add_argument(
            '--claim-id',
            type=int,
            help='ID específico del reclamo a verificar'
        )
        parser.add_argument(
            '--recent',
            action='store_true',
            help='Verificar solo reclamos recientes (últimas 24 horas)'
        )

    def handle(self, *args, **options):
        claim_id = options.get('claim_id')
        recent_only = options.get('recent')
        
        self.stdout.write(
            self.style.SUCCESS('🔍 Verificando estado de emails...')
        )
        
        if claim_id:
            # Verificar reclamo específico
            try:
                claim = ClaimRequest.objects.get(id=claim_id)
                self.verify_single_claim(claim)
            except ClaimRequest.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'❌ Reclamo #{claim_id} no encontrado')
                )
        else:
            # Verificar múltiples reclamos
            queryset = ClaimRequest.objects.all().order_by('-created_at')
            
            if recent_only:
                # Solo reclamos de las últimas 24 horas
                yesterday = timezone.now() - timedelta(days=1)
                queryset = queryset.filter(created_at__gte=yesterday)
                self.stdout.write(
                    self.style.WARNING('📅 Verificando solo reclamos de las últimas 24 horas...')
                )
            
            self.verify_multiple_claims(queryset)

    def verify_single_claim(self, claim):
        """Verifica un reclamo específico"""
        self.stdout.write(f'\n📋 Reclamo #{claim.id}:')
        self.stdout.write(f'   👤 {claim.full_name}')
        self.stdout.write(f'   📧 {claim.email}')
        self.stdout.write(f'   📅 {claim.created_at.strftime("%d/%m/%Y %H:%M")}')
        
        # Verificar estado del email
        email_status = get_email_status(claim)
        if email_status == "Enviado recientemente":
            self.stdout.write(
                self.style.SUCCESS(f'   📧 Estado: {email_status}')
            )
        elif email_status == "Enviado":
            self.stdout.write(
                self.style.SUCCESS(f'   ✅ Estado: {email_status}')
            )
        else:
            self.stdout.write(
                self.style.ERROR(f'   ❌ Estado: {email_status}')
            )
        
        # Verificar envío
        if verify_email_sent(claim):
            self.stdout.write(
                self.style.SUCCESS('   ✅ Verificación: Email enviado')
            )
        else:
            self.stdout.write(
                self.style.ERROR('   ❌ Verificación: Error en envío')
            )

    def verify_multiple_claims(self, queryset):
        """Verifica múltiples reclamos"""
        total_claims = queryset.count()
        sent_emails = 0
        error_emails = 0
        
        self.stdout.write(f'\n📊 Total de reclamos a verificar: {total_claims}')
        
        for claim in queryset:
            email_status = get_email_status(claim)
            
            if email_status in ["Enviado", "Enviado recientemente"]:
                sent_emails += 1
                status_icon = "✅"
            else:
                error_emails += 1
                status_icon = "❌"
            
            self.stdout.write(
                f'{status_icon} #{claim.id} - {claim.email} - {email_status}'
            )
        
        # Resumen
        self.stdout.write(f'\n📈 Resumen:')
        self.stdout.write(
            self.style.SUCCESS(f'   ✅ Emails enviados: {sent_emails}')
        )
        self.stdout.write(
            self.style.ERROR(f'   ❌ Errores: {error_emails}')
        )
        
        if total_claims > 0:
            success_rate = (sent_emails / total_claims) * 100
            self.stdout.write(
                self.style.SUCCESS(f'   📊 Tasa de éxito: {success_rate:.1f}%')
            )
