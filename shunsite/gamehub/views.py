import articles as articles
from .models import _get_articles, _create_articles, _get_articles_by_id, _del_articles_by_id, _edit_articles_by_id, \
    create_articles, Articles, create_user, booking, cc
from .create_articles import create_articles_form, edit_articles_form

from django.http import HttpResponse, request, JsonResponse, HttpResponseNotFound
from django.template import loader
from django.shortcuts import render, redirect
from django.views.decorators.http import  require_http_methods

from .form import django_form
from .upload import UploadFileForm
from .login import login_form
import os
from .login import login_form
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.core.paginator import Paginator

import logging
loader =logging.getLogger(('django'))

# Create your views here.

def get_session(request):
    request.session['pref'] = "C++"
    response = HttpResponse(" Session Set! ")
    return  response

def set_session(request):
    response = HttpResponse(" Session Set!" + str(request.session['pref']))
    return  response

## - -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - --

def get_cookies(request):
    if "pref" in request.COOKIES:
        print("pref", request.COOKIES['pref'])
        response = HttpResponse("～小鳥飛來 吃掉麵包屑～")

def cookies(request):
    response = HttpResponse("麵包掉了～")
    response.set_cookie("pref","PYTHON")
    return response

## - -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - --


def index(request):
    articles = _get_articles()
    content = {"articles":articles}
    return render(request,'index.html',content)

    # return render(request,'index.html',{"form":login_form})


## - -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - --
## - -- - -- - --  -- - -- - -- <    極 為 重 要      >>- -- -- - -- - --  -- - -- - --
## - -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - --



@require_http_methods(['POST'])
def comments(request):
    d_form = django_form(request.POST)
    if d_form.is_valid():
        print("這個評論 沒問題！")
    else:
        print("這個評論 糟糕了？")
    context ={"form":d_form}

    # Save Comments
    content = request.POST.get('content')
    create_article(content)
    return HttpResponse("評論已上傳 完畢！")
    # return  render(request,"articles.html".context)

## - -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - --

def show_orderlist(request):
    # return HttpResponse("恭喜！目前已建立成功，即將顯示預約項目： ")
    return render(request,"show_orderlist.html") ## 直接回應 bookingAgame 這個網頁畫面

# def commts(request):
#     return HttpResponse("再確認一次，即將預約的內容是...： ")

# @require_http_methods(['POST'])
def creat_per_no(request):
    # Save DAtA
    # return HttpResponse("您已開始建立預約內容＠＿＠")
    return render(request,"bookingAgame.html") ## 直接回應 bookingAgame 這個網頁畫面
    # return redirect('show_orderlist')
    # return redirect('commts')

def creat_per_no_shun(request):
    # print("p1")
    # booking()
    # create_user()
    cc()
    # render(request, "bookingAgame.html")  ## 直接回應 bookingAgame 這個網頁畫面
    return HttpResponse("還行吧，您已開始建立預約內容＠＿＠ shunZ 想不到吧")
## - -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - --


# @cache_page(10)
def author(request):
    articles =cache.get("root")
    if not articles:
        articles = _get_articles()
        cache.set("root",articles,30)

    paginator = Paginator(articles,2)

    context = {
        "name" : "Snoopy",
        "sidebar" : ["Home","Articles","Authors"],
        "articles": articles
    }
    return render(request,"author.html", context)

def login(request):
    if not request.user.is_authenticated:
        print("沒人在誒！")
        return render(request, 'login.html')
    print("功能正在被啟動中....")
    return redirect("index")

def usr_login(request):
    user = authenticate(request, username= request.POST.get('username'), password= request.POST.get('password'))
    # user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    # return redirect('usr_login')
    if user is not None:
        # auth_login(request, user)
        # print("--< 登入成功 >--")
        # return redirect('usr_login')

        # - # - # - # - # - # - # - # - # - #
        form = django_form()
        # if request.user.is_authenticated:
        #     context = {"form": form, "user": request.user.username}
        # else:
        #     context = {"form": form, "user": ""}

        context = {"form": form, "user": request.user.username}
        return render(request, "articles.html", context)

    else:
        print(">-- 登入失敗 --< ")
        # return redirect('index')
        return render(request, "login.html")

def usr_logout(request):
    auth_logout(request)
    # return HttpResponse(" 登入失敗 ＴＡＴ ")
    return redirect('index')

## - -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - --

def article(request,a_num):

    form = django_form()
    if request.user.is_authenticated:
        context = {"form": form,"user":request.user.username}
    else:
        context = {"form": form,"user":""}
    return render(request, "articles.html", context)


def view_article(request,a_id):
    context = { "article" : _get_articles_by_id(a_id) }
    return render(request, "show_articles.html", context)

def create(request):
        create_user()
        return HttpResponse("使用者已建立完成")

def create_article(request):
    _create_articles(request)
    return redirect("index")

# def create_article(request):
#
#     if request.method == 'POST':
#         _create_articles(request)
#         return redirect("index")
#     else:
#         form = create_articles_form()
#         content = {"form":form,"user":""}
#         return render(request,"create_articles.html",content)

def edit_article(request,id):
    if request.method == 'POST':
        _edit_articles_by_id(request,id)
        return redirect("index")
    else:
        form = edit_articles_form(id)
        context = {"form":form,"id": id}
        return render(request,"edit_articles.html",context)

def delete_article(request,id):
    _del_articles_by_id(id)
    return redirect("index")

def get__article(request):
    user = auth_login.objects.get(username="root")
    return Articles.object.filter(user = user).all().order_by("-last_update")

## - -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - --


