from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from blog.models import Profile
from .forms import SignUpForm, EditProfileForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'web_page', 'facebook_url', 'instagram_url', 'linkedin_url']
    success_url = reverse_lazy('home')


class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'registration/create_profile.html'
    form_class = ProfilePageForm
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)