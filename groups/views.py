from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Group
from .forms import GroupForm


def index(request):
    return redirect('group-list')


class GroupListView(ListView):
    model = Group
    paginate_by = 10


class GroupDetailView(DetailView):
    model = Group


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm

    def get_success_url(self):
        return reverse('group-detail', kwargs={'pk': self.object.id})


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/group_form.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse('group-detail', kwargs={'pk': self.object.id})


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'groups/group_confirm_delete.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'name'

    def get_success_url(self):
        return reverse('group-list')
