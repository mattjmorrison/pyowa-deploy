from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from sample.models import person


class People(ListCreateAPIView):
    model = person.Person


class Person(RetrieveUpdateDestroyAPIView):
    model = person.Person
