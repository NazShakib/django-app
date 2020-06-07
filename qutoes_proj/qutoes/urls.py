from django.urls import path
from . import views 

urlpatterns = [
    path('',views.QutoesView.as_view(), name='index')

]