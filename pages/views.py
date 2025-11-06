from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Page
from .forms import PageForm

class PageListView(ListView):
    model = Page
    template_name = 'pages/list.html'
    context_object_name = 'pages'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().order_by('-id')
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q) | qs.filter(subtitle__icontains=q)
        return qs

class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/detail.html'
    context_object_name = 'page'

class OwnerOrStaffMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object() if hasattr(self, 'get_object') else None
        return self.request.user.is_staff or (obj and obj.author == self.request.user)

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/create.html'
    success_url = reverse_lazy('pages:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Página creada correctamente.')
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, OwnerOrStaffMixin, UpdateView):  # mixin (g)
    model = Page
    form_class = PageForm
    template_name = 'pages/update.html'
    success_url = reverse_lazy('pages:list')

    def form_valid(self, form):
        messages.success(self.request, 'Página actualizada.')
        return super().form_valid(form)

class PageDeleteView(LoginRequiredMixin, OwnerOrStaffMixin, DeleteView):
    model = Page
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('pages:list')

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, 'Página eliminada.')
        return super().delete(request, *args, **kwargs)