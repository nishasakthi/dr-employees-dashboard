from django.db import models

class Hundred(models.Model):
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=20)
    department = models.CharField(max_length=10)
    salary = models.IntegerField()

    def __str__(self):
        return self.employee_name
