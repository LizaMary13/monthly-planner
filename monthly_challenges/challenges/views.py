from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

challenges = {
    'january': 'Exercise daily!',
    'february': 'Skin, mind and physical health!',
    'march': 'Prepare dresses and finalise designs!',
    'april': 'D-Day is nearly here!!!',
    'may': 'Off we go - fresh start!',
    'june': 'Work, work, work!',
    'july': None,
    'august': 'Liya\'s month!',
    'september': 'Workout!',
    'october': 'Pray everyday!',
    'november': 'Back HOME!',
    'december': 'First Christmas at HOME!'
}

def index(request):
    list_months = ""
    months = list(challenges.keys())
    # list_months += "<ul>"
    # for month in months:
    #     list_months += f"<li><a href=\"{reverse('monthly-plan', args=[month])}\">{month.capitalize()}</a></li>"
    # list_months += "</ul>"
    context = {'months': months}
    return render(request, 'challenges/index.html', context)

def monthly_plan_by_number(request, month):
    months = list(challenges.keys())
    try:
        month_chosen = months[month-1]
        resp = challenges[month_chosen]
        return HttpResponseRedirect(reverse('monthly-plan', args=[month_chosen]))
    except:
        # return HttpResponseNotFound(f'<h2>Requested month not found!</h2>') -- OR
        return HttpResponseNotFound(render_to_string('404.html'))


def monthly_plan(request, month):
    months = list(challenges.keys())
    if month.lower() in months:
        return render(request, 'challenges/challenge.html', {'text': challenges[month], 'month': month})
    else:
        # return HttpResponseNotFound(f'<h2>Requested month not found!</h2>') -- OR
        return HttpResponseNotFound(render_to_string('404.html'))
    
    
    
    