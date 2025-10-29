from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from core.models import Task, Tag


# Create your views here.


class TasksListView(ListView):
    model = Task
    paginate_by = 5
    template_name = "core/index.html"
    queryset = Task.objects.prefetch_related("tags")



class TagListView(ListView):
    model = Tag
    paginate_by = 5
    template_name = "core/tag_list.html"



class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("core:tag-list")
    template_name = "core/tag_form.html"


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("core:tag-list")
    template_name = "core/tag_form.html"


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("core:tag-list")
    template_name = "core/tag_confirm_delete.html"