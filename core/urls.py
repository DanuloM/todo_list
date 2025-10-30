from django.urls import path

from core.views import TasksListView, TagListView, TagUpdateView, TagCreateView, TagDeleteView, TaskCreateView, \
    TaskUpdateView, TaskDeleteView, ToggleComplete

urlpatterns = [
    path("", TasksListView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/toggle_complete/", ToggleComplete.as_view(), name="toggle-complete"),
]

app_name = "core"
