from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('show', views.show, name='show'),
    path('editpage/<int:pk>', views.editpage, name='editpage'),
    path('edit_product/<int:pk>', views.edit_product, name='edit_product'),
    path('deletepage/<int:pk>', views.deletepage, name='deletepage'),
]
