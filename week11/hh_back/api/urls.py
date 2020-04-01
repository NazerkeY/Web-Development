from django.urls import path
from api.views import company_list, vacancy_list, company_one, vacancy_one, company_vacancy, vacancy_top

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_one),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_one),
    path('companies/<int:id>/vacancies/', company_vacancy),
    path('vacancies/top_ten/', vacancy_top)
]