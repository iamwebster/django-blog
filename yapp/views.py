from typing import Any
from django.db.models.query import QuerySet
from .models import Post 
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import AddPageForm, RegisterUserForm, LoginUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login


class HomePage(ListView):
    model = Post 
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 5
    def search_query(self):
        return self.request.GET.get('search', '')


class DetailPage(DetailView):
    model = Post
    template_name = 'detail.html'
    

def add_page(request):
    error = ''
    if request.method == 'POST':
        form = AddPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form was incorrect'


    form = AddPageForm()
    return render(request, 'add_page.html', context={'form_data': form, 'error': error})

# class AddPost(CreateView):
#     model = Post 
#     template_name = 'add_page.html'
#     form_class = AddPageForm


class DeletePost(DeleteView):
    model = Post 
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    def get_success_url(self) -> str:
        return reverse_lazy('home')
    



def logout_user(request):
    logout(request)
    return redirect('home')

