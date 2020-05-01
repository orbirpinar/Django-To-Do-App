from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from todoapp.models import TodoItem
from todoapp.forms import AddItemForm

def TodoView(request):
	if request.method=='POST':
		form = AddItemForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo')
	else:		
		form = AddItemForm()
	items = TodoItem.objects.all()
	return render(request,'todo.html',{'items':items,'form':form})

def DeleteTodo(request,todo_id):
	delete_item =TodoItem.objects.filter(id=todo_id).first()
	delete_item.delete()
	return redirect('todo')

def CompleteTodo(request,todo_id):
	item = TodoItem.objects.filter(id=todo_id).first()
	item.complete = not item.complete
	item.save()
	return redirect('todo')

