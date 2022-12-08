from rest_framework import viewsets, permissions
from .models import EmployeeModel
from .serializers import EmployeeSerializer

class EmployeesList(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        return EmployeeModel.objects.all()


class EmployeeViewset(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [ permissions.IsAuthenticated]
    #lookup_field = "id"

    def get_queryset(self):
        return EmployeeModel.objects.all()   #filter(owner=self.request.user)#pk=self.lookup_url_kwarg  
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

