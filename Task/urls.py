from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('StudentCreate',views.StudentCreate,name='StudentCreate'),
    path('StudentDelete',views.StudentDelete,name='StudentDelete'),
    path('StudentShow',views.StudentShow,name='StudentShow'),
    path('StudentUpdate',views.StudentUpdate,name='StudentUpdate'),
]
