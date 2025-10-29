from django.shortcuts import render
from django.views.generic import ListView

from core.models import Task, Tag


# Create your views here.


class TasksListView(ListView):
    model = Task
    paginate_by = 5
    template_name = "core/index.html"
    queryset = Task.objects.prefetch_related("tags")



class TagsListView(ListView):
    model = Tag
    paginate_by = 5
    template_name = "core/tag_list.html"