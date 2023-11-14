from .models import Post 
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import AddPageForm, RegisterUserForm, LoginUserForm, UpdatePostForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login


class HomePage(ListView):
    model = Post 
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-time_updated']
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
            submission = form.save(commit=False)
            submission.author = request.user
            submission.save()
            return redirect('home')
        else:
            error = 'Form was incorrect'


    form = AddPageForm()
    return render(request, 'add_page.html', context={'form_data': form, 'error': error})


class DeletePost(DeleteView):
    model = Post 
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class UpdatePost(UpdateView):
    model = Post 
    form_class = UpdatePostForm
    template_name = 'update_post.html'
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


def search_post(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        post_search = Post.objects.filter(title__contains=searched)
        return render(request, template_name='search.html', context={'searched': searched, 'post_search': post_search})
    else:
        return render(request, template_name='search.html', context={})