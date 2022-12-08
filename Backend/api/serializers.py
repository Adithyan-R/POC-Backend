from rest_framework import serializers
from api.models import EmployeeModel

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeModel
        fields = ['id','name','department','designation','phonenumber']

