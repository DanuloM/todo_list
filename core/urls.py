from django.urls import path

from core.views import TasksListView

urlpatterns = [
    path("", TasksListView.as_view(), name="index"),
]


app_name = "core"