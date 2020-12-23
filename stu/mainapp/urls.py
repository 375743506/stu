"""
author:skr
datetime:2020/12/23 16:20
reversion:1.0
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index')
]
