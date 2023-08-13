from django.urls import path
from .views import index, top_sellers
from django.conf import settings

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers')
]
