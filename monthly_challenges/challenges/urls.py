from django.urls import path, include
from challenges.views import *

urlpatterns = [
    path('', index, name="index"),
    path('<int:month>', ChallengesView.as_view()),
    path('<str:month>', ChallengesView.as_view(), name='monthly-plan'),
    path('add/<str:month>', add_new, name="add_new"),
    path('delete/<int:plan_id>', delete_plan, name='delete_plan'),
    path('edit/<int:plan_id>', edit_plan, name='edit_plan'),
    path('update/<int:plan_id>', update_plan, name='update_plan'),
    # path('mark_complete/<int:plan_id>', mark_complete, name='mark-complete')
]