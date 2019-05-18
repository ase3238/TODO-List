from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Todo
from .forms import TodoForm

# Create your views here.

class TodoLV(ListView):
	model = Todo
	template_name = 'todolist/index.html'
	context_object_name = 'todos'
	paginate_by = 10
	
class TodoDV(DetailView):
	model = Todo
	template_name = 'todolist/detail.html'
	
class TodoCreV(CreateView):
	form_class = TodoForm
	template_name = 'todolist/create_form.html'

class TodoUpdV(UpdateView):
	model = Todo
	form_class = TodoForm
	template_name = 'todolist/edit_form.html'

class TodoDelV(DeleteView):
	model = Todo
	success_url = reverse_lazy('todo:todo_index')
	template_name = 'todolist/delete_form.html'

def done(request, todo_id):
	todo = get_object_or_404(Todo, pk=todo_id)
	todo.done = not todo.done
	todo.save()
	return HttpResponseRedirect(reverse('todo:todo_detail', args=(todo.id,)))

