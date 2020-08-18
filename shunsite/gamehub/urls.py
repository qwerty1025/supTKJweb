from  django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),

    path('articles', views.view_article, name="articles"),
    path('articles/<int:a_id>', views.view_article, name="articles"),
    path('author', views.author, name="author"),
    path('signin', views.login, name="login"),
    path('articles/edit/<int:id>', views.edit_article, name="edit_article"),
    path('articles/delete/<int:id>', views.delete_article, name="delete_article"),
    path('articles/create', views.create_article, name="create_article"),


    ## 阿順隔一晚，再試試看@ 0818
    path('show_orderlist',views.show_orderlist,name="show_orderlist"),
    path('bookingAgame',views.creat_per_no,name="bookingAgame"),

    # path('commts',views.commts,name="commts"),
    # path('booking', views.booking, name="booking"),
    path('creat_per_no_shun', views.creat_per_no_shun, name="creat_per_no_shun"),



    path('comments', views.comments, name="comments"),
    path('create', views.create, name="create"),

    path('login' , views.usr_login, name="usr_login"),     # backends function
    path('logout', views.usr_logout, name="usr_logout"),  # backends function

    path('cookies', views.cookies, name="cookies"),  # backends function
    path('get_cookies', views.get_cookies, name="get_cookies"),  # backends function

    path('get_session', views.get_session, name="get_session"),  # backends function
    path('set_session', views.set_session, name="set_session"),  # backends function

]
