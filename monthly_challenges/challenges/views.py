import logging
import datetime
import requests

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from challenges.models import *
from challenges.serializers.plan import PlanDetailSerializer
from monthly_challenges.settings import DATE_FACTS_API, QUOTES_API

log = logging.getLogger('api')

# Create your views here.


class ChallengesView(APIView):

    def get(self, request, month):
        try:
            if (isinstance(month, int)):
                month_chosen = Month.objects.get(month=month)
                month = month_chosen.get_month_display()
                # return HttpResponseRedirect(reverse('monthly-plan', args=[month_chosen]))
            else:              
                months = Month.objects.all()
                for each_month in months:
                    if each_month.get_month_display().lower() == month.lower():
                        month_chosen = each_month
                        break
            quote, author = None, None
            quote_resp = requests.get(QUOTES_API).json()
            quote = quote_resp.get('text', None)
            author = quote_resp.get('author', {}).get('name', None)
            challenges = Plan.objects.filter(month=month_chosen).order_by('day')
            return render(request, 'challenges/challenge.html', {'challenges': challenges, 'month': month, \
                "author": author, "quote": quote})
             # return HttpResponseNotFound(f'<h2>Requested month not found!</h2>')
        except Exception as e:
            log.error(e)
            return HttpResponseNotFound(render_to_string('404.html'))
        
        
    def post(self, request, month):
        try:
            data = {}
            months = Month.objects.all()
            for each in months:
                if each.get_month_display().lower() == month.lower():
                    month = each
                    break
            data_receieved = dict(request.data)
            data['day'] = int(data_receieved['day'][0])
            data['month'] = month.id
            data['title'] = data_receieved['title'][0]
            serializer = PlanDetailSerializer(data=data)
            
            if serializer.is_valid():
                serializer.save()
                return render(request, 'challenges/saved.html')
            else:
                log.error(serializer.errors)
                return HttpResponseNotFound(render_to_string('errors.html'))
        except Exception as e:
            log.error(e)
            return HttpResponseNotFound(render_to_string('errors.html'))
        
        
def delete_plan(request, plan_id):
    try:
        plan = Plan.objects.get(id=plan_id)
        plan.delete()
        return render(request, 'challenges/saved.html')
    except Exception as e:
        log.error(e)
        return HttpResponseNotFound(render_to_string('errors.html'))
    
    
def edit_plan(request, plan_id):
    try:
        plan = Plan.objects.get(id=plan_id)
        return render(request, 'challenges/edit.html', {'plan': plan})
    except Exception as e:
        log.error(e)
        return HttpResponseNotFound(render_to_string('errors.html'))
   
 
@api_view(['POST'])
def update_plan(request, plan_id):
    try:
        data = {}
        data_received = dict(request.data)
        # import pdb; pdb.set_trace()
        data['title'] = data_received['title'][0]
        data['day'] = int(data_received['day'][0])
        plan = Plan.objects.get(id=plan_id)
        serializer = PlanDetailSerializer(plan, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'challenges/saved.html')
        else:
            log.error(serializer.errors)
            return HttpResponseNotFound(render_to_string('errors.html'))
    except Exception as e:
        log.error(e)
        return HttpResponseNotFound(render_to_string('errors.html'))
        
    
def index(request):
    list_months = ""
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", \
        "October", "November", "December"]
    # list_months += "<ul>"
    # for month in months:
    #     list_months += f"<li><a href=\"{reverse('monthly-plan', args=[month])}\">{month.capitalize()}</a></li>"
    # list_months += "</ul>"
    date = datetime.datetime.now().day
    month = datetime.datetime.now().month
    today_facts_api = requests.get(f"{DATE_FACTS_API}/{month}/{date}/date?json")
    facts = today_facts_api.json()['text']
    context = {'months': months, 'facts': facts}
    return render(request, 'challenges/index.html', context)

def add_new(request, month):
    return render(request, 'challenges/new.html', {"month": month})

# @api_view(['POST'])
# def mark_complete(request, plan_id):
#     import pdb; pdb.set_trace()
#     print(request.data)
#     return render(request, 'challenges/saved.html')