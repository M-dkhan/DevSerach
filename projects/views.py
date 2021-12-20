from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def projects(request):
    return HttpResponse("Thi site is working")


def project(request,pk):
    return HttpResponse("Thi site is working")
