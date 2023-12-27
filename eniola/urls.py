from django.urls import path
from eniola import views


urlpatterns = [
    path('', views.contact, name='contact'),
    path('success', views.success, name='success')
]
