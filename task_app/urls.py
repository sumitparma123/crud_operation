from django.urls  import path
from . import views
urlpatterns = [
      path('signup',views.Registration.as_view(),name="signup"),
      path('login',views.Logins.as_view(),name="login"),
      path('logout',views.logouts,name="logout"),
      path('',views.show,name="show"),
      path('home',views.home,name="home"),
      path('delete',views.delete,name='delete'),
      path('update',views.update,name='update'),
      path('add_product',views.add_product,name='add_product'),

]
