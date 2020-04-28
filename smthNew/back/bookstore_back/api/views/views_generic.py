from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# from api.models import Company, Vacancy

# from api.serializers import CompanySerializer, VacancySerializer


class CompanyListAPIView(generics.ListCreateAPIView):
    pass


class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    pass


class VacancyListAPIView(generics.ListCreateAPIView):
    pass


class VacancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    pass
