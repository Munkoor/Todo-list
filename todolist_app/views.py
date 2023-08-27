from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View

from list.models import Task, Tag


class TasklistView(generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "list/todo_list.html"
    ordering = ["-is_completed"]


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todolist:task-list")
    template_name = "list/task_form.html"


class TaskToggleStatusView(View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.is_completed = not task.is_completed
        task.save()
        return redirect("todolist:task-list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5
    template_name = "list/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")
    template_name = "list/tag_form.html"


class TagUpdateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")
    template_name = "list/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "list/tag_confirm_delete.html"
    success_url = reverse_lazy("todolist:tag-list")
