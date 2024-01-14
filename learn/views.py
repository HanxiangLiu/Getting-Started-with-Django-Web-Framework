from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from learn.models import Author, Course


def index(request):
    return HttpResponse('Hello Shiyanlou.')


def courses(request):
    courses = Course.objects.all()
    return render(request, 'learn/courses.html', {'courses': courses})


def course(request, id):
    course = Course.objects.get(id=id)
    date = datetime.now()
    context = {'course': course, 'date': date}
    return render(request, 'learn/course.html', context)


def login(request, methods=['GET', 'POST']):
    if request.method == 'GET':
        name = request.COOKIES.get('name') or 'Stranger'
        sessionid = request.COOKIES.get('sessionid')
        if request.session.exists(sessionid):
            resp = HttpResponse(f'您已处于登录状态，{name}')
            return resp
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name == 'shiyanlou' and password == 'hello':
            request.session['name'] = name
            resp = HttpResponse(f'登录成功，{name}')
            resp.set_cookie('name', name, 60 * 5, path='/learn')
            return resp
    return render(request, 'learn/login.html', {'name': name})


def search(request, methods=['GET', 'POST']):
    name = request.POST.get('name')
    try:
        author = Author.objects.get(name=name) if name else None
    except Author.DoesNotExist:
        author = None
    courses = Course.objects.filter(author=author) if author else []
    return render(request, 'learn/search.html', {'courses': courses})
