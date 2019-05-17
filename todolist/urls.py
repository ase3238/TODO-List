from django.conf.urls import url
from todolist import views

urlpatterns = [
	url(r'^$', views.TodoLV.as_view(), name='todo_index'),
	url(r'^[0-9]*/$'), views.TodoDV.as_view(), name='todo_detail'),

	url(r'^form/$'), views.TodoCreV.as_view(), name='todo_form'),
	url(r'^[0-9]*/edit/$'), views.TodoUpdV.as_view(), name='todo_edit'),
	url(r'^[0-9]*/delete/$'), views.TodoDelV.as_view(), name='todo_delete'),
	
	url(r'^done/$'), views.done, name='todo_done'),
]
