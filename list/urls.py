from django.urls import path

from list.views import TasklistView, TagListView, TagCreateView, TagUpdateView, \
    TagDeleteView

urlpatterns = [
    path("", TasklistView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todolist"
