from django.urls import path
from eniola import views


urlpatterns = [
    path('', views.index, name='index'),
    path('success', views.success, name='success')
]
