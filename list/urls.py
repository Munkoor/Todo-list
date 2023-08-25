from django.urls import path

from list.views import TasklistView, TagListView, TagCreateView, TagUpdateView, \
    TagDeleteView, TaskToggleStatusView, TaskCreateView

urlpatterns = [
    path("", TasklistView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("<int:pk>/toggle-status/", TaskToggleStatusView.as_view(),
         name="task-toggle-status"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create")
]

app_name = "todolist"
