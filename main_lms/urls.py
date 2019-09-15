from django.urls import path
from .import views 
from django.contrib.auth import views as auth_views
urlpatterns = [  
    #path('admin/', admin.site.urls),
    path('', views.viewshome, name="index"),
    path('viewsforall/studetails/<int:id>/', views.studetails, name="studetails"),
    path('viewsforall/booksdetails/<int:id>/', views.booksdetails, name="booksdetails"), 
    path('viewsforall/viewsnews/', views.viewsnews, name="viewsnews"),

    path('news/news/', views.news, name="news"),
    path('news/nedit/<int:id>/', views.nedit, name="nedit"),
    path('news/ndelete/<int:id>/', views.ndelete, name="ndelete"), 
    path('news/newscomments/<int:id>/', views.newscomments, name="newscomments"),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),  
    path('accounts/reg_form/',views.register, name="register"),

    path('accounts/profile/',views.profile, name="profile"),
    path('books/binsert/', views.binsert, name="binsert"),  
    path('books/blist/',views.blist, name="blist"), 
    path('books/bedit/<int:id>/', views.bedit, name="bedit"),  
    path('books/bupdate/<int:id>/', views.bupdate, name="bupdate"),
    path('books/bdelete/<int:id>/', views.bdelete, name="bdelete"), 

    path('cbooks/cbtype/', views.cbtype, name="cbtype"), 
    path('cbooks/cbdelete/<int:id>/', views.cbdelete, name="cbdelete"),
    path('cbooks/cbshelf/', views.cbshelf, name="cbshelf"), 
    path('cbooks/cbsdelete/<int:id>/', views.cbsdelete, name="cbsdelete"),

    path('borrow/brinsert/', views.brinsert, name="brinsert"),  
    path('borrow/brlist/',views.brlist, name="brlist"),
    path('borrow/bredit/<int:id>/', views.bredit, name="bredit"),  
    path('borrow/brupdate/<int:id>/', views.brupdate, name="brupdate"),
    path('borrow/brdelete/<int:id>/', views.brdelete, name="brdelete"),

    path('students/sinsert/', views.sinsert, name="sinsert"),  
    path('students/slist/',views.slist, name="slist"),
    path('students/sdelete/<int:id>/', views.sdelete, name="sdelete"),
    path('students/sedit/<int:id>/', views.sedit, name="sedit"),  
    path('students/supdate/<int:id>/', views.supdate, name="supdate"),

    path('cstudents/cdepttype/', views.cdepttype, name="cdepttype"), 
    path('cstudents/cdeptdelete/<int:id>/', views.cdeptdelete, name="cdeptdelete"),
    path('cstudents/csession/', views.csession, name="csession"), 
    path('cstudents/csessiondelete/<int:id>/', views.csessiondelete, name="csessiondelete"), 

     
    path('setting/headercolor/', views.headercolor, name="headercolor"),
    path('setting/chcolor/', views.chcolor, name="chcolor"),
    path('setting/activitylog/', views.activitylog, name="activitylog"),
    path('setting/fine/', views.fine, name="fine"),
    path('setting/fineenter/', views.fineenter, name="fineenter"),

    path('bsearch/', views.bsearch, name="bsearch"),
    path('btsearch/', views.btsearch, name="btsearch"),
    path('ballsearch/', views.ballsearch, name="ballsearch"),

    path('brnsearch/', views.brnsearch, name="brnsearch"),
    path('brbdsearch/', views.brbdsearch, name="brbdsearch"),
    
    path('snsearch/', views.snsearch, name="snsearch"),
    path('sdsearch/', views.sdsearch, name="sdsearch"),
    path('sallsearch/', views.sallsearch, name="sallsearch"),
    path('isearch/', views.isearch, name="isearch"),

    path('rtbooks/', views.rtbooks, name="rtbooks"),

    path('about/project/', views.project, name="projects"),
    path('about/developers/', views.developers, name="developers"),


   # path('emp/', views.emp, name="emp"),  
]  