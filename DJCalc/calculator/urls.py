from django.urls import path

from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path('add',views.addition, name='add'),
	path('sub',views.subtract, name='sub'),
	path('multi',views.multiply, name='multi'),
	path('div',views.divide, name='div')
]
# when 'localhost:8000' is called, the function 'index' will be called in 'views.py'
