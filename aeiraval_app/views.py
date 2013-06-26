# Create your views here.
from django.http import HttpResponse
from aeiraval_app.models import Family


def test(request): 
    family = Family.objects.all()[0]
    return HttpResponse(family.name)
