from django.shortcuts import render
from rest_framework import views, viewsets, mixins
from .serializers import PulseSerializer
from .models import Pulse


# Create your views here.
class PulseViewSet(viewsets.ModelViewSet):
    queryset = Pulse.objects.all()
    serializer_class = PulseSerializer
