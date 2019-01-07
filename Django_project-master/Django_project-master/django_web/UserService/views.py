from django.shortcuts import render
from .models import NewTable
from django.shortcuts import render_to_response, redirect

from django.http import HttpResponse

from .forms import UserForm, LoginForm

from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate

from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt
import json
from .models import NewTable
import datetime
from django.contrib.auth import(

    authenticate,

    login as django_login,

    logout as django_logout,

)

def index(request):
    if not request.user.is_authenticated:

        data = {"username":request.user, "is_authenticated":request.user.is_authenticated}

    else:

        data = {"last_login":request.user.last_login, "username":request.user.username,

        "password":request.user.password,"is_authenticated":request.user.is_authenticated}

    return render(request, "UserService/index.html", context= {"data":data} )

def visual(request):
    return render(request, "UserService/Plot 20.html")

@csrf_exempt

def signup(request):

    if request.method == "POST":

        form = UserForm(request.POST)

        if form.is_valid():

            new_user = User.objects.create_user(**form.cleaned_data)

            login(request, new_user)

            return redirect('/')

        else:

            return HttpResponse('사용자명이 이미 존재합니다.')

    else:

        form = UserForm()

        return render(request, "UserService/signup.html", {'form': form})



def login_check(request):

    if request.method =="POST":

        form = LoginForm(request.POST)

        username = request.POST["username"]

        password = request.POST["password"]

        user = authenticate(username = username, password = password)

        if user is not None:

            django_login(request, user)

            return redirect("/")

        else:

            return render("UserService/index.html.",{"msg":"로그인 실패, 다시시도해주세요"})

    else:

        form = LoginForm()

        return render(request, "UserService/login.html", {"form":form})



def logout(request):

    django_logout(request)

    return redirect("/")







def result(request):

    print("---------results()-------------")

    testtable = NewTable.objects.all()

    context = {'testtable': testtable}

    return render(request, 'UserService/result.html', context)

def chart1(request):
    abc = []
    sdw = []
    data = {}
    testtable = NewTable.objects.all()
    i = 0
    for value in testtable:
        abc.append(value.min_tem)
        sdw.append(value.max_tem)
        data = {
            'min_tem' : abc ,
            'max_tem' : sdw
    }
    print(data.keys())
    return HttpResponse(json.dumps(data), content_type="application/json")

def htmldd(request):
    return render(request, 'UserService/test.html', {})



def chart2(request):
    testtable = NewTable.objects.filter(date__gte=datetime.date(2018, 1, 1),
            date__lte=datetime.date(2018, 12, 13)).values('max_power')
    t = testtable.values()
    context = {
        'info' : t
    }
    return render(request, 'UserService/index.html', context)

def chart3(request):
    testtable1 = NewTable.objects.filter(date__gte=datetime.date(2018, 1, 1),
        date__lte=datetime.date(2018, 1, 31)).values_list('avg_tem')
    testtable6 = NewTable.objects.filter(date__gte=datetime.date(2018, 6, 1),
            date__lte=datetime.date(2018, 6, 30)).values_list('avg_tem')
    
    print(testtable6)
    a = []
    b = []
    for i in testtable1:
        a.append(i)
    for i in testtable6:
        b.append(i)
    context = {
        'jan' : a,
        'jun' : b,
    }
    print(type(context))

    return HttpResponse(json.dumps(context), content_type="application/json")


def htmldd2(request):
    return render(request, 'UserService/test.html', {})

