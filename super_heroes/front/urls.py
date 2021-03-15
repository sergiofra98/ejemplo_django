from . import views
from django.urls import path

urlpatterns = [    
    path('', views.home, name='home'),
    path('heroe-list', views.heroeList, name='heroe-list'),
    path('heroe-create', views.heroeCreate, name='heroe-create'),
    path('heroe-update/<int:id>', views.heroeUpdate, name='heroe-update'),
    path('heroe-delete/<int:id>', views.heroeDelete, name='heroe-delete'),
    path('poder-list', views.poderList, name='poder-list'),
    path('poder-create', views.poderCreate, name='poder-create'),
    path('poder-update/<int:id>', views.poderUpdate, name='poder-update'),
    path('poder-delete/<int:id>', views.poderDelete, name='poder-delete'),
]