from django.urls import path

from app.views import index, landing, stats


urlpatterns = [
    path('index/', index, name='index'),
    path('landing/', landing, name='landing'),
    path('stats/', stats, name='stats'),
]
