from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AbandonedAccountsSectionViewSet,
    AccountTypeViewSet,
    YearlyDocumentViewSet,
    ContractCategoryViewSet,
    AccountContractsSectionViewSet,
    ContractViewSet,
    ClaimRequestViewSet,
    FraudReportViewSet,
    RightsAndDutiesPageViewSet,
    ServiceRatesPageViewSet,
    ServiceCategoryViewSet,
    ProvinceViewSet,
    SuggestionBoxViewSet,
    SuggestionBoxPageViewSet,
    FraudReportPageViewSet,
    ClaimRequestPageViewSet
)

router = DefaultRouter()
router.register(r'abandoned-accounts', AbandonedAccountsSectionViewSet, basename='abandoned-accounts')
router.register(r'account-types', AccountTypeViewSet, basename='account-types')
router.register(r'yearly-documents', YearlyDocumentViewSet, basename='yearly-documents')
router.register(r'contract-categories', ContractCategoryViewSet, basename='contract-categories')
router.register(r'account-contracts', AccountContractsSectionViewSet, basename='account-contracts')
router.register(r'contracts', ContractViewSet, basename='contracts')
router.register(r'claim-requests', ClaimRequestViewSet, basename='claim-requests')
router.register(r'fraud-reports', FraudReportViewSet, basename='fraud-reports')
router.register(r'rights-and-duties', RightsAndDutiesPageViewSet, basename='rights-and-duties')
router.register(r'service-rates', ServiceRatesPageViewSet, basename='service-rates')
router.register(r'service-categories', ServiceCategoryViewSet, basename='service-categories')
router.register(r'provinces', ProvinceViewSet, basename='provinces')
router.register(r'suggestion-box', SuggestionBoxViewSet, basename='suggestion-box')
router.register(r'suggestion-box-page', SuggestionBoxPageViewSet, basename='suggestion-box-page')
router.register(r'fraud-report-page', FraudReportPageViewSet, basename='fraud-report-page')
router.register(r'claim-request-page', ClaimRequestPageViewSet, basename='claim-request-page')

app_name = 'prousuario'

urlpatterns = [
    path('user-support/', include(router.urls)),
]
