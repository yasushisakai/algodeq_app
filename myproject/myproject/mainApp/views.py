import json

from __builtin__ import locals
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import Http404,HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from myproject.settings import MEDIA_URL,BASE_DIR,test_path,MEDIA_ROOT
from django.contrib.syndication.views import Feed

from myproject.mainApp.models import User,Plan

# Create your views her

def getPlansAll(request):
    '''
    gets every plan
    '''

    plans = Plan.objects.all()

    return render_to_response('main_obsolete.html',
        {
            'plans':plans
        },
        context_instance = RequestContext(request)
    )

    #return HttpResponse([p.name for p in plans])


def treeSearch(_array,_plan):
    for a in _array:
        if a['id'] == _plan.relation.id:
            a['children'].append({'id':_plan.id, 'name':_plan.name, 'geometry':_plan.geometry, 'children':[]})
        else:
            treeSearch(a['children'],_plan)


def getRecursiveAll(request):
    '''
    gets plan in a recursive json format.
    '''

    plans = Plan.objects.all()
    rec_plans = []

    for p in plans:

        if len(rec_plans)<1:
            rec_plans.append({'id':p.id,'name':p.name,'geometry':p.geometry,'children':[]})
        else:
            treeSearch(rec_plans,p)

    return render_to_response('main.html',
        {
            'plans':json.dumps(rec_plans)
        },
        context_instance = RequestContext(request)
    )

    #print json.dumps(rec_plans)


def getRecursiveAllTest(request):
    '''
    gets plan in a recursive json format.
    '''

    plans = Plan.objects.all()
    rec_plans = []

    for p in plans:

        if len(rec_plans)<1:
            rec_plans.append({'id':p.id,'name':p.name,'geometry':p.geometry,'children':[]})
        else:
            treeSearch(rec_plans,p)

    return render_to_response('tree.html',
        {
            'plans':json.dumps(rec_plans)
        },
        context_instance = RequestContext(request)
    )

    #print json.dumps(rec_plans)


def signin(request):
        return render_to_response('sign_in.html',
        {

        },
        context_instance = RequestContext(request)
        )


def getPlan(request,id):
    '''
    gets single plan
    '''

    plan  = Plan.objects.get(id=id)

    return render_to_response('single_plan.html',
        {
            'plan':plan
        },
        context_instance = RequestContext(request)
        )

    #return HttpResponse(plan[0].name)

def getUser(request,userId):
    '''
    gets single user
    '''

    user = User.objects.get(id=userId)

    return render_to_response('singleUser.html',
        {
            'user':user
        },
        context_instance = RequestContext(request)
        )

   # return HttpResponse(user[0].name)


def ajax_test(request):
    if request.method == 'POST' and request.is_ajax():
        name = request.POST['name']
        city = request.POST['city']
        message = name + 'lives in' + city

        return HttpResponse(json.dumps({'message': message}))
    return 




def batch(request):
    return render_to_response('batch.html',context_instance = RequestContext(request))

def batchAddUser(request):
    from myproject.mainApp.functions import addUserRandom
    number = int(request.GET['number'])
    addUserRandom(number)

    operation = 'add user (%i)'%number
    operation_messsage = 'added %i users.'%number

    return render_to_response('batch_operation.html',locals())

def batchDeleteUser(request):
    #delete users
    User.objects.all().delete()

    operation = 'delete user'
    operation_message = 'terminated user'

    return render_to_response('batch_operation.html',locals())

def batchAddPlan(request):
    from myproject.mainApp.functions import addPlanRandom
    number = int(request.GET['number'])
    addPlanRandom(number)

    operation = 'add plan(s) (%i)'%number
    operation_messsage = 'added %i plan(s).'%number

    return render_to_response('batch_operation.html',locals())

def batchDeletePlan(request):
    #delete users
    Plan.objects.all().delete()

    operation = 'delete plan'
    operation_message = 'terminated plans'

    return render_to_response('batch_operation.html',locals())

def diffTest(request):
    return render_to_response('testing.html',context_instance=RequestContext(request))

def saveImage(request):
    image_data = request.POST['img'].decode("base64")
    image_file = open(MEDIA_ROOT+"/plans/test.png","wb")
    image_file.write(image_data)
    image_file.close()
    return render_to_response('testing.html',context_instance=RequestContext(request))
