from django.urls import path
from .views import products,products_id
urlpatterns = [
    path('postdata/',products),
    path('getdata/<int:id>/',products_id),
]


