from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from api.models import Vacancy, Company
from api.serializers import VacancySerializer, CompanySerializerWithVacancies

class VacancyListAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticated,)

class VacancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class CompanyWithVacancies(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializerWithVacancies