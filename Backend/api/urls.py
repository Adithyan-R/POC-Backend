
from rest_framework import routers

from django.urls import path, include
from .api import EmployeeViewset 
from .api import EmployeesList
app_name = "api"
router = routers.DefaultRouter()
router.register('employee',EmployeeViewset,basename='employee')
router.register('emplist',EmployeesList,basename='emplist')
urlpatterns = [
    path('', include(router.urls)),
]

