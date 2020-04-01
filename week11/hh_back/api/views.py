from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from api.models import Company, Vacancy
from django.http import Http404

def company_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe = False)

def company_one(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        raise Http404
    return JsonResponse(company.to_json())

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe = False)

def vacancy_one(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id = vacancy_id)
    except Vacancy.DoesNotExist as e:
        raise Http404
    return JsonResponse(vacancy.to_json())

def company_vacancy(request, id):
    vacancies = Vacancy.objects.all()
    main_info = []
    for item in vacancies:
        if item.company_id.id == id:
            main_info.append(item.to_json())
    return JsonResponse(main_info, safe = False)

def vacancy_top(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)
