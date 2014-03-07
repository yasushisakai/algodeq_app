
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



def getPlan(request,planId):
    '''
    gets single plan
    '''

    plan  = Plan.objects.get(id = planId)

    #return render_to_response('singlePlan.html',
    #    {
    #        'post':plan[0]
    #    },
    #    context_instance = RequestContext(request)
    #    )

    return HttpResponse(plan[0].name)

def getUser(request,userId):
    '''
    gets single user
    '''

    user = User.objects.get(id=userId)

    #return render_to_response('singleUser.html',
    #    {
    #        'user':user[0]
    #    },
    #    context_instance = RequestContext(request)
    #    )

    return HttpResponse(user[0].name)