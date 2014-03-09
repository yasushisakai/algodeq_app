from __builtin__ import locals
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import Http404,HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from myproject.settings import MEDIA_URL,BASE_DIR,test_path
from django.contrib.syndication.views import Feed

from myproject.mainApp.models import User,Plan

# Create your views her

def getPlansAll(request):
    '''
    gets every plan
    '''

    plans = Plan.objects.all()

    return render_to_response('main.html',
        {
            'plans':plans
        },
        context_instance = RequestContext(request)
    )

    #return HttpResponse([p.name for p in plans])

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


