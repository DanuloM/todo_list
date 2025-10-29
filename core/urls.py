from django.urls import path

from core.views import TasksListView, TagListView, TagUpdateView, TagCreateView

urlpatterns = [
    path("", TasksListView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>", TagUpdateView.as_view(), name="tag-update"),
]

app_name = "core"
