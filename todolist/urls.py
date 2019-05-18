from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
	path('', views.TodoLV.as_view(), name='todo_index'),
	path('<int:pk>/', views.TodoDV.as_view(), name='todo_detail'),

	path('form/', views.TodoCreV.as_view(), name='todo_create'),
	path('<int:pk>/edit/', views.TodoUpdV.as_view(), name='todo_edit'),
	path('<int:pk>/delete/', views.TodoDelV.as_view(), name='todo_delete'),
	
	path('<int:todo_id>/done/', views.done, name='todo_done'),
]
