from django.urls import reverse_lazy
from django.views import generic

from list.models import Task, Tag


class TasklistView(generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "list/todo_list.html"


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
