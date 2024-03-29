from django.shortcuts import render


def home(request):
    return render(request, 'front/home.html')

def page_not_found(request, exception):
    '''404 错误处理函数
    '''

    return render(request, '404.html')

def server_error(request):
    '''500 服务器内部异常处理函数
    '''
    return render(request, '500.html')