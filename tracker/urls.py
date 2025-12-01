

from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('register/',views.register,name="register_page"),
    path('',views.login_view,name="login_page"),
    path('logout/',views.logout_view,name="logout_view"),
    path('delete_transaction<id>',views.delete_transaction,name='delete_transaction'),
]