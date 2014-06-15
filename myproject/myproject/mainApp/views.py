import json
import datetime

import Image

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth

from myproject.mainApp.admin import UserCreationForm
from myproject.settings import MEDIA_ROOT
from myproject.mainApp.models import Plan


def index(request):
    """
    view function for 'index.html'
    """

    if log_in(request):  # authentication process
        return HttpResponse("logged in!")

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


def single_plan(request, name):
    """
    gives the information of a single_plan
    single_plan.html is used as template
    """

    if log_in(request):  # authentication process
        return HttpResponse("logged in!")

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
        'plan_json': plan_json,
    }, context_instance=RequestContext(request)
    )


def make(request, plan_id):
    """
    quite same as the single_plan function
    this just gets the plan by id, and the rest is done by js
    make.html is used as template
    """

    if log_in(request):  # authentication process
        return HttpResponse("logged in!")

    plan = Plan.objects.get(id=plan_id)

    if request.method == 'POST' and request.is_ajax():

        new_plan_name = request.POST['new_plan_name']
        new_plan_geometry = request.POST['new_plan_geometry']
        new_plan_similarity = float(request.POST['new_plan_similarity'])

        if request.POST['phase'] == "0":
            validation = plan.validate_new_plan(
                new_plan_name,
                new_plan_geometry,
                new_plan_similarity,
            )
            return HttpResponse(json.dumps(validation))
        else:

            # get the image data from server and decode it.
            new_plan_image_data = request.POST['image']  # image is only sent in phase 1
            new_plan_image_data = new_plan_image_data.decode("base64")
            image_name = 'img_' + new_plan_name + '.png'
            image_name_large = 'img_' + new_plan_name + '_large.png'

            # save image to server.
            image_path = MEDIA_ROOT + "/plans/" + image_name_large
            image_file = open(MEDIA_ROOT + image_path, "wb")
            image_file.write(new_plan_image_data)
            image_file.close()

            image_path_small = MEDIA_ROOT + "/plans/small/" + image_name
            Image.open(image_path).resize((100, 200)).save(image_path_small)

            new_plan_cost = request.POST['new_plan_cost']

            # update the users creation_time
            request.user.update_creation_time()

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

    # below happens there is neither post nor ajax
    plan_json = plan.get_json()

    return render_to_response('make.html', {
        'plan': plan,
        'plan_json': plan_json
    }, context_instance=RequestContext(request)
    )


def finalize(request):
    if request.method == 'POST' and request.is_ajax():
        if "name" in request.POST:

            test_name = request.POST["name"]
            flag = False
            try:
                plan = Plan.objects.get(name=test_name)
            except:
                flag = True
            print flag
            return HttpResponse(json.dumps({"flag": flag}))

        elif "save_name" in request.POST:

            new_plan_name = request.POST['save_name']

            # get the image data from server and decode it.
            new_plan_image_data = request.POST['save_image']  # image is only sent in phase 1
            new_plan_image_data = new_plan_image_data.decode("base64")
            image_name = 'img_' + new_plan_name + '.png'

            # save image to server.
            image_path = MEDIA_ROOT + "/plans/" + image_name
            image_file = open(image_path, "wb")
            image_file.write(new_plan_image_data)
            image_file.close()

            image_path_small = MEDIA_ROOT + "/plans/small/" + image_name
            Image.open(image_path).resize((128, 144)).save(image_path_small)

            new_plan_cost = request.POST['save_cost']

            # update the users creation_time
            request.user.update_creation_time()


            # save and add plan
            new_plan = Plan(
                name=new_plan_name,
                creation_time=datetime.datetime.now(),
                image_file=MEDIA_ROOT + '/plans/' + image_name,
                geometry=request.POST['save_geometry'],
                similarity=request.POST['save_similarity'],
                points_inborn=request.POST['save_points'],
                points_acquired=0.0,
                architect=request.user,
                cost=request.POST['save_cost'],
                parent_plan=Plan.objects.get(id=request.POST['save_parent_id'])
            )
            new_plan.save()
            return HttpResponse()

    geometry = request.POST['new_geometry']
    similarity = float(request.POST['new_similarity'])

    parent_id = int(request.POST['parent_id'])
    parent_name = request.POST['parent_name']
    parent_points = float(request.POST['parent_points'])

    return render_to_response('finalize.html', {
        'geometry': geometry,
        'similarity': similarity,
        'parent_id': parent_id,
        'parent_name': parent_name,
        'parent_points': parent_points,
    }, context_instance=RequestContext(request)
    )


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


def log_in(request):
    """
    authentication process
    will be used in all views except finalize and sign-up
    """

    if 'email' in request.POST and request.is_ajax():
        print 'hi'
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(email=email, password=password)

        print 'auth.authenticate'

        if user is not None and user.is_active:
            auth.login(request, user)
            print 'auth.login'
            return True

    return False


def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect("/")




