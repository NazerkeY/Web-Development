from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default = '')
    city = models.CharField(max_length=250)
    address = models.TextField(default='')

    def to_json(self):
        return{
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'city':self.city,
            'address':self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(default='')
    salary = models.FloatField()
    company_id = models.ForeignKey(Company, on_delete = models.CASCADE, default=1)


    def to_json(self):
        return{
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'salary':self.salary,
            'company':self.company_id.to_json()
        }