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

# Create your views here

# index


def index(request):
    if 'email' in request.POST:
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if (not user is None) and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("../")
        else:
            return render(request, 'obsolete/index.html')
    else:
        return render(request, 'obsolete/index.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("../")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('../')
    else:
        form = UserCreationForm()

    return render_to_response("obsolete/signup.html", {
        'form': form,
    }, context_instance=RequestContext(request))


def getPlansAll(request):
    '''
    gets every plan
    '''

    plans = Plan.objects.all()

    return render_to_response('obsolete/main_obsolete.html',
                              {
                                  'plans': plans
                              },
                              context_instance=RequestContext(request)
    )


#return HttpResponse([p.name for p in plans])

def treeSearch(_array, _plan):
    for a in _array:
        if a['id'] == _plan.relation.id:
            a['children'].append(
                {'id': _plan.id, 'name': _plan.name, 'parent': _plan.relation.id, 'geometry': _plan.geometry,
                 'children': []})
        else:
            treeSearch(a['children'], _plan)


def getRecursiveAll(request):
    '''
    gets plan in a recursive json format.
    '''

    plans = Plan.objects.all()
    rec_plans = []

    for p in plans:

        if len(rec_plans) < 1:
            rec_plans.append(
                {'id': p.id, 'name': p.name, 'parent': None, 'geometry': json.loads(p.geometry), 'children': []})
        else:
            treeSearch(rec_plans, p)


    #time
    sec_create = request.user.next_creation()
    sec_eval = request.user.next_evaluation()

    return render_to_response('obsolete/main.html',
                              {
                                  'rawPlans': plans,
                                  'nums': len(plans),
                                  'plans': json.dumps(rec_plans),
                                  'sec_create': sec_create,
                                  'sec_eval': sec_eval
                              },
                              context_instance=RequestContext(request)
    )


def getRecursiveAll2(request):
    '''
    gets plan in a recursive json format.
    '''

    plans = Plan.objects.all()
    rec_plans = []

    for p in plans:

        if len(rec_plans) < 1:
            rec_plans.append({'id': p.id, 'name': p.name, 'geometry': json.loads(p.geometry), 'children': []})
        else:
            treeSearch(rec_plans, p)

    return render_to_response('obsolete/main2.html',
                              {
                                  'rawPlans': plans,
                                  'nums': len(plans),
                                  'plans': json.dumps(rec_plans)
                              },
                              context_instance=RequestContext(request)
    )


def getRecursiveAllTest(request):
    '''
    gets plan in a recursive json format.
    '''

    plans = Plan.objects.all()
    rec_plans = []

    for p in plans:

        if len(rec_plans) < 1:
            rec_plans.append({'id': p.id, 'name': p.name, 'geometry': p.geometry, 'children': []})
        else:
            treeSearch(rec_plans, p)

    return render_to_response('obsolete/tree.html',
                              {
                                  'plans': json.dumps(rec_plans)
                              },
                              context_instance=RequestContext(request)
    )

    #print json.dumps(rec_plans)


def getPlan(request, id):
    '''
    gets single plan
    '''

    plan = Plan.objects.get(id=id)
    user = plan.user

    return render_to_response('obsolete/single_plan.html',
                              {
                                  'plan': plan,
                                  'creator': user,
                                  #'geom': json.dumps(plan.geometry)
                                  'geom': plan.geometry
                              },
                              context_instance=RequestContext(request)
    )

    #return HttpResponse(plan[0].name)


def getUser(request, userId):
    '''
    gets single user
    '''

    user = User.objects.get(id=userId)

    return render_to_response('singleUser.html',
                              {
                                  'user': user
                              },
                              context_instance=RequestContext(request)
    )

    # return HttpResponse(user[0].name)


def ajax_test(request):
    print request.is_ajax()

    if request.method == 'POST' and request.is_ajax():
        print request.POST['frame']
        image_data = request.POST['image'].decode("base64")
        img_name = 'img_' + request.POST['frame'] + '_' + datetime.datetime.now().strftime("%y%m%d%H%M%S") + '.png'
        image_file = open(MEDIA_ROOT + "/plans/" + img_name, "wb")
        image_file.write(image_data)
        image_file.close()
        message = "successfully uploaded " + img_name

        return HttpResponse(json.dumps({'message': message}))

    return render(request, 'obsolete/ajax.html')


def canvas_test(request):
    if request.method == 'POST' and request.is_ajax():
        image_data = request.POST['image'].decode("base64")
        #img_name = 'img_' + datetime.datetime.now().strftime("%y%m%d%H%M%S") + '.png'
        img_name = 'frame_' + request.POST['frame'] + '.png'
        image_file = open(MEDIA_ROOT + "/frames/" + img_name, "wb")
        image_file.write(image_data)
        image_file.close()
        message = "successfully uploaded " + img_name

        return HttpResponse(json.dumps({'message': message}))

    plans = Plan.objects.all()

    return render_to_response('canvas_samples/canvas_sample7.html',
                              {
                                  'geomData': plans,
                              },
                              context_instance=RequestContext(request)
    )


####################################################
## BATCH operations
####################################################


def batch_add_user(request):
    from myproject.mainApp.obsolete.functions import addUserRandom

    number = int(request.GET['number'])
    addUserRandom(number)

    operation = 'add user (%i)' % number
    operation_message = 'added %i users.' % number

    return render_to_response('obsolete/batch_operation.html', locals())


def batch_delete_user(request):
    if request.user.is_authenticated() and request.user.is_staff():

        #delete users
        User.objects.all().delete()

        #add admin user
        admin = User.objects.create_superuser('admin@admin.com', 'admin', 'admin')

        operation = 'deleted user'
        operation_message = 'terminated user. Added user \'admin\''

        return render_to_response('obsolete/batch_operation.html', locals())
    else:
        operation = 'delete user failed'
        operation_message = 'failed to terminate user, please login in a admin account'


def batch_add_plan(request):
    from myproject.mainApp.obsolete.functions import addPlanRandom2

    number = int(request.GET['number'])
    addPlanRandom2(number)

    operation = 'add plan(s) (%i)' % number
    operation_messsage = 'added %i plan(s).' % number

    return render_to_response('obsolete/batch_operation.html', locals())


def batch_delete_plan(request):
    #delete users
    Plan.objects.all().delete()

    operation = 'delete plan'
    operation_message = 'terminated plans'

    return render_to_response('obsolete/batch_operation.html', locals())


#####################################################
## miscellaneous
#####################################################


def saveImage(request):
    image_data = request.POST['img'].decode("base64")
    image_file = open(MEDIA_ROOT + "/plans/test.png", "wb")
    image_file.write(image_data)
    image_file.close()
    return render_to_response('obsolete/diffTest.html', context_instance=RequestContext(request))