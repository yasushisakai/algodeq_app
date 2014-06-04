import json
import datetime
from __builtin__ import locals

from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth

from myproject.mainApp.admin import UserCreationForm
from myproject.settings import MEDIA_ROOT
from myproject.mainApp.models import User, Plan


def index(request):
    plans = Plan.objects.all()
    plans_json = []

    for p in plans:
        if len(plans_json) < 1:

            plans_json.append({
                'id': p.id,
                'name': p.name,
                'url': p.get_absolute_url(),
                'parent': None,
                'geometry': p.geometry,
                'children': []})
        else:
            Plan.tree_search(plans_json, p)

    return render_to_response('index.html', {
        'plans': plans,
        'plans_num': len(plans),
        'plans_json': json.dumps(plans_json)
    }, context_instance=RequestContext(request))


def single_plan(request, name):
    plan = Plan.objects.get(name=name)

    return render_to_response('single_plan.html', {
        'plan': plan,
        'plan_json': plan.get_json()
    }, context_instance=RequestContext(request)
    )
