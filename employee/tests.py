from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Hundred

class HundredAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.employee_1 = Hundred.objects.create(
            employee_id=25,
            employee_name="Micheal Jackson",
            department="HR",
            salary=1700000
        )

        self.employee_2 = Hundred.objects.create(
            employee_id=35,
            employee_name="William Jackson",
            department="Sales",
            salary=5200000
        )

        self.valid_payload = {
            "employee_id": 5,
            "employee_name": "William Shake",
            "department": "HR",
            "salary": 87564533
        }

        self.invalid_payload = {
            "employee_id": 9,
            "employee_name": "",
            "department": "",
            "salary": 5678884
        }

    def test_get_all_employees(self):
        response = self.client.get('/employees-list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_employee_valid(self):
        response = self.client.get(f'/employee-detail/{self.employee_1.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["employee_name"], self.employee_1.employee_name)

    def test_get_single_employee_invalid(self):
        response = self.client.get('/employee-detail/987')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_employee_valid(self):
        response = self.client.post('/employees-list/', data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Hundred.objects.count(), 3)

    def test_create_employee_invalid(self):
        response = self.client.post('/employees-list/', data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST) 

    # def test_update_employee_valid(self):
    #     updated_payload = {
    #         "employee_id": 52,
    #         "employee_name": "William Shakes",
    #         "department": "Sales",
    #         "salary": 97564533
    #     }
    #     response = self.client.put(f'/employee-detail/{self.employee_1.id}/', data=updated_payload, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.employee_1.refresh_from_db()
    #     self.assertEqual(self.employee_1.employee_name, "William Shakes")

    def test_updated_employee_invalid(self):
        response = self.client.put(f'/employee-detail/{self.employee_1.id}', data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST) 

    def test_deleted_employee_valid(self):
        response = self.client.delete(f'/employee-detail/{self.employee_1.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Hundred.objects.count(), 1)

    def test_deleted_employee_invalid(self):
        response = self.client.delete('/employee-detail/879')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


