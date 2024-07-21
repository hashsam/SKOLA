from django.shortcuts import redirect,render
from app.models import Categories,Course,Level,Video,UserCource,Payment
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib import messages
from .settings import*
from django.contrib.auth.decorators import login_required
from time import time
import datetime


def BASE(request):
    return render(request,'base.html')


def HOME(request):
    category= Categories.objects.all().order_by('id')[0:5]
    course=Course.objects.filter(status='PUBLISH').order_by('-id')

    context={
        'category':category,
        'course':course,
    }
    return render(request,'main/home.html',context)


def SINGLE_COURSE(request):
    category=Categories.get_all_category(Categories)
    level=Level.objects.all()
    course=Course.objects.all()
    FreeCourse_count =Course.objects.filter(price = 0).count()
    PaidCourse_count =Course.objects.filter(price__gt = 1).count()

    context={
        'category':category,
        'level':level,
        'course':course,
        'FreeCourse_count':FreeCourse_count,
        'PaidCourse_count':PaidCourse_count,
    }
    return render(request,'main/single_course.html',context)

def filter_data(request):
    category = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')

    if price == ['priceFree']:
       course = Course.objects.filter(price=0)
    elif price == ['pricePaid']:
       course = Course.objects.filter(price__gte=1)
    elif price == ['priceAll']:
       course = Course.objects.all()
    elif category:
       course = Course.objects.filter(category__id__in=category).order_by('-id')
    elif level:
       course = Course.objects.filter(level__id__in = level).order_by('-id')
    else:
       course = Course.objects.all().order_by('-id')   
   
   
    context = {
        'course':course,
    }
    t = render_to_string('ajax/course.html',context)
    return JsonResponse({'data': t})

def CONTACT_US(request):
    category= Categories.get_all_category(Categories)
    context = {
       'category': category,
    }
    return render(request,'main/contact_us.html',context)

def ABOUT_US(request):
    category= Categories.get_all_category(Categories)
    context = {
       'category': category,
    }
    return render(request,'main/about_us.html')

def SEARCH_COURSE(request):
    category= Categories.get_all_category(Categories)
    
    query= request.GET['query']
    course=Course.objects.filter(title__icontains = query)
    context = {
        'course':course,
        'category': category,
    }
    return render(request,'search/search.html',context)

def COURSE_DETAILS(request,slug):
    category= Categories.get_all_category(Categories)
    time_duration= Video.objects.filter(course__slug=slug).aggregate(sum=Sum('time_duration'))
    course = Course.objects.filter(slug=slug)
    if course.exists():
        course = course.first()
    else:
        return render('404')

    context={
        'course':course,
        'category': category,
        'time_duration':time_duration,
    }    
    return render(request,'course/course_details.html',context)

def PAGE_NOT_FOUND(request):
    category= Categories.get_all_category(Categories)
    context = {
       'category': category,
    }
    return render(request,'error/404.html',context)

def CHECKOUT(request,slug):
    course=Course.objects.get(slug=slug)
    action=request.GET.get('action')
    order=None

    context={
        'course':course,
        'order':order,
    }
    return render(request,'checkout/checkout.html',context)

@login_required
def MY_COURSE(request):
    course=UserCource.objects.filter(user=request.user)

    context={
        'course':course,
    }
    return render(request,'course/my_course.html',context)


def VERIFY_PAYMENT(request):
    return render(request,'verify_payment/success.html')