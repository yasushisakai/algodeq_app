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
    """
    view funtion for 'index.html'
    """
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
    """
    gives the information of a single_plan
    single_plan.html is used as template
    """

    plan = Plan.objects.get(name=name)  # plan is needed in both situations

    if request.method == 'POST' and request.is_ajax():
        plan.add_points()
        plan.architect.update_evaluation_time()  # update model evaluation time of user
        return HttpResponse(json.dumps({'message': 'added points'}))

    # below happens when there is neither post nor ajax
    plan_json = plan.get_json()

    return render_to_response('single_plan.html', {
        'plan': plan,
        'plan_json': plan_json
    }, context_instance=RequestContext(request)
    )


def make(request, plan_id):
    """
    quite same as the single_plan function
    this just gets the plan by id, and the rest is done by js
    make.html is used as template
    """
    plan = Plan.objects.get(id=plan_id)

    if request.method == 'POST' and request.is_ajax():
        new_plan_name = request.POST['new_plan_name']
        new_plan_geometry = request.POST['new_plan_geometry']
        new_plan_similarity = float(request.POST['new_plan_similarity'])

        if request.POST['phase'] == "0":
            validation = plan.validate_new_plan(
                new_plan_name,
                new_plan_geometry,
                new_plan_similarity
            )
            return HttpResponse(json.dumps(validation))
        else:
            #save and add plan
            print new_plan_geometry
            new_plan = Plan(
                name=new_plan_name,
                creation_time=datetime.datetime.now(),
                image_file='',  # todo fetch image file
                geometry=new_plan_geometry,
                similarity=new_plan_similarity,
                points_inborn=new_plan_similarity*plan.get_total_points(),
                points_acquired=0.0,
                architect=request.user,
                parent_plan=plan
            )
            new_plan.save()

            print request.POST['phase']

    # below happens there is neither post nor ajax
    plan_json = plan.get_json()

    return render_to_response('make.html', {
        'plan': plan,
        'plan_json': plan_json
    }, context_instance=RequestContext(request)
    )

