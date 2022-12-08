from django.urls import path, reverse, include, resolve
from rest_framework.routers import DefaultRouter
from django.test import SimpleTestCase
from api.api import EmployeeViewset
from api.models import EmployeeModel
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView



class EmployeeApiTests(APITestCase):
    
    employees_url = reverse('api:employee-list')
    

    def setUp(self):
        self.user = User.objects.create_user(
            username='admin',email='admin@admin,com', password='admin')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


    def test_get_employee_authenticated(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.employees_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee_un_authenticated(self):
        
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.employees_url)
        self.assertEquals(response.status_code, 401)

    def test_post_employee_authenticated(self):
        
        data = {
            "name": "Adam",
            "department": "QA",
            "designation": "Tester",
            "phonenumber": "9842678324"
        }
        self.client.force_authenticate(self.user)
        response = self.client.post(self.employees_url, data, format='json') 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class EmployeeUpdateDeleteTests(APITestCase):

     #kwargs={'pk':1}('http://127.0.0.1:8000/api/employee/')

    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)

        self.emp = EmployeeModel.objects.create(id='3',name='Eve',department= "IT",designation="Analyst", phonenumber="943767384")
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        #employees_url = reverse('api:employee-detail',kwargs={'pk':self.emp.pk})

    def test_update_employee_autheticated(self):
        self.client.force_authenticate(self.user)
        #emp = EmployeeModel.objects.get()
        employees_url = reverse('api:employee-detail',kwargs={'pk':self.emp.pk})
        print(employees_url)


        data = {
            "id":"1",
            "name": "Eve",
            "department": "IT",
            "designation": "Engineer",
            "phonenumber": "943767384"
        }
        response =self.client.put(employees_url, data, format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_delete_employee_authenticated(self):
        self.client.force_authenticate(self.user)
        employees_url = reverse('api:employee-detail',kwargs={'pk':self.emp.pk})
        
        response = self.client.delete(employees_url)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

