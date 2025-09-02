from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class BaseViewSet(viewsets.ModelViewSet):
    """
    Base viewset with common functionality.
    """
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if hasattr(instance, 'soft_delete'):
            instance.soft_delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return super().destroy(request, *args, **kwargs)