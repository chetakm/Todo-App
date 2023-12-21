from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from .models import Todo


# Create your views here.
@login_required
def index(request):
    # item_list = Todo.objects.all()
    item_list = Todo.objects.filter(user=request.user)
    print(item_list)
    if request.method == 'POST':
        title = request.POST.get('title')
        details = request.POST.get('details')
        if title and details:
            data = Todo.objects.create(user=request.user,title=title, details=details)
            data.save()
        else:
            return HttpResponse("Enter All Details")
        return redirect('index')

    return render(request, 'mytodo/index.html', {'tasks': item_list})


def delete_task_view(request, task_id):
    # task = get_object_or_404(Task, pk=task_id)
    task = Todo.objects.get(id=task_id)
    task.delete()

    return redirect('index')
