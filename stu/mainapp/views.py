from django.shortcuts import render, redirect, reverse, get_list_or_404, get_object_or_404
from .models import *
# Create your views here.
from django.http import HttpResponse


def index(request):

    return render(request, 'index.html', locals())
