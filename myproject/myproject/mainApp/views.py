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

    log_in(request)  # authentication process.

    # add one plan (tokyo) if there is nothing
    if len(Plan.objects.all()) < 1:
        Plan.init_plan()

    plans = Plan.objects.all()
    plans_json = []

    for p in plans:
        if len(plans_json) < 1:

            plans_json.append({
                'id': p.id,
                'name': p.name,
                'architect': p.architect.username,
                'url': p.get_absolute_url(),
                'parent': None,
                # 'geometry': p.geometry,
                'similarity': p.similarity,
                'creation_time': '2014/01/01,0:0:0',
                'total_points': p.get_total_points(),
                'cost': p.cost,
                'children': []})
        else:
            Plan.tree_search(plans_json, p)

    return render_to_response('index.html', {
        'plans': plans,
        'plans_num': len(plans),
        'plans_json': json.dumps(plans_json)
    }, context_instance=RequestContext(request))


def sign_up(request):
    """
    view for signing up(register)
    """

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print form
            form.save()
            print 'redirect'
            return HttpResponseRedirect('../')
    else:
        form = UserCreationForm()

    return render_to_response("sign_up.html",
                              {
                                  'form': form,
                              },
                              context_instance=RequestContext(request))


def single_plan(request, name):
    """
    gives the information of a single_plan
    single_plan.html is used as template
    """

    log_in(request)  # autheication process

    plan = Plan.objects.get(name=name)  # plan is needed in both situations

    if request.method == 'POST' and request.is_ajax():
        points = float(request.POST['points'])
        added_points = plan.add_points(points)
        plan.architect.update_evaluation_time()  # update model evaluation time of user
        return HttpResponse(json.dumps({'points_added': added_points}))

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

    log_in(request)  # authentication process

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

            # get the image data from server and decode it.
            new_plan_image_data = request.POST['image']  # image is only sent in phase 1
            new_plan_image_data = new_plan_image_data.decode("base64")
            image_name = 'img_' + new_plan_name + '.png'

            # save image to server.
            image_file = open(MEDIA_ROOT + "/plans/" + image_name, "wb")
            image_file.write(new_plan_image_data)
            image_file.close()

            new_plan_cost = request.POST['new_plan_cost']

            # save and add plan
            new_plan = Plan(
                name=new_plan_name,
                creation_time=datetime.datetime.now(),
                image_file=MEDIA_ROOT + '/plans/' + image_name,
                geometry=new_plan_geometry,
                similarity=new_plan_similarity,
                points_inborn=new_plan_similarity * plan.get_total_points(),
                points_acquired=0.0,
                architect=request.user,
                cost=new_plan_cost,
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


def log_in(request):
    """
    authentication process
    will be used in all views except finalize and sign-up
    """

    if 'email' in request.POST:
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        user = auth.authenticate(email=email,password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            print 'logged in'
            return HttpResponse('logged in as ' + user.username)





