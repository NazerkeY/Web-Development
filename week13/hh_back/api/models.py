from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=300)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default='')
    salary = models.FloatField()
    company_id = models.ForeignKey(Company, on_delete = models.CASCADE, default=1, related_name='vacancies')

    def __str__(self):
        return f'Vacancy id: {self.id}'

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'company_id': self.company_id.to_json()
        }

    def full(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company_id': self.company_id
        }