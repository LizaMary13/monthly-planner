from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:month>', views.monthly_plan_by_number),
    path('<str:month>', views.monthly_plan, name='monthly-plan')
]