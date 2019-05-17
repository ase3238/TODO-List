from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from todolist.models import Todo

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
	model = Todo
	fields = ['title', 'description', 'priority', 'due']
	template_name = 'todolist/create_form.html'

class TodoUpdV(UpdateView):
	model = Todo
	fields = ['title', 'description', 'priority', 'due']
	template_name = 'todolist/edit_form.html'

class TodoDelV(DeleteView):
	model = Todo
	success_url = reverse_lazy('todo_index')
	template_name = 'todolist/delete_form.html'

def done(request, todo_id):
	todo = get_object_or_404(Todo, pk=todo_id)
	todo.done = not todo.done
	todo.save()
	return HttpResponseRedirect(reverse('todo:todo_detail', args=(todo.id,)))

