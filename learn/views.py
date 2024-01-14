from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# 引入所需映射类
from .models import Course


def index(request):
    return HttpResponse("Hello Shiyanlou.")


def courses(request):
    courses = Course.objects.all()
    return render(request, 'learn/courses.html', {'courses': courses})


def course(request, id, method=['GET']):
    course = Course.objects.get(id=id)
    date = datetime.now()
    context = {'course': course, 'date': date}
    return render(request, 'learn/course.html', context)

def add_a_b(request, a, b):
    return HttpResponse(a+b)

def login(request, methods=['GET', 'POST']):
    if request.method == 'GET':
        name = request.COOKIES.get('name')
        sessionid = request.COOKIES.get('sessionid')
        if request.session.exists(sessionid):
            resp = HttpResponse('您已处于登录状态，{}'.format(name))
            return resp
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name == 'shiyanlou' and password=='hello':
            request.session['name'] = name
            resp = HttpResponse('登录成功，{}'.format(name))
            resp.set_cookie('name', name, 60 * 5, path='/learn')
            return resp
    return render(request, 'learn/login.html', {'name': name})