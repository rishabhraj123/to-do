from django.shortcuts import render, redirect

# Create your views here.
from .models import Task,Taskheading
from .forms import TaskForm,TaskHeadForm

def index(request):
	if not request.user.is_authenticated:
		context = {}
	else:
		headings = Taskheading.objects.filter(user__username__contains=request.user)
		tasks = {}
		for heading in headings:
			task = Task.objects.filter(heading = heading)
			tasks[heading] = task
		form = TaskForm()
		context = {'tasks':tasks,'form':form}
	return render(request, 'tasks/home.html',context)


def updatetask(request, id):
	task = Task.objects.get(id=id)
	form = TaskForm(instance=task)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
		return redirect('home')
	context = {'form':form}
	return render(request, 'tasks/update_task.html', context)


def deletetask(request, id):
	task = Task.objects.get(id=id)
	if request.method == 'POST':
		task.delete()
		return redirect('home')
	context = {'task':task}
	return render(request, 'tasks/delete.html', context)


def addheading(request):
	if not request.user.is_authenticated:
		context = {}
	else:
		form = TaskHeadForm()
		if request.method =='POST':
			form = TaskHeadForm(request.POST)
			if form.is_valid():
				heading = form.save(commit=False)
				heading.user = request.user
				heading.save()
			return redirect('home')
		context = {'form':form}
	return render(request,'tasks/addheading.html',context)


def addtask(request,id):
	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			heading = Taskheading.objects.get(id=id)
			form = form.save(commit=False)
			form.heading = heading
			form.save()
	return redirect('home')