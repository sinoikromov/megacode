from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ClientForm, RegisterUser, AdminClientForm
from .models import Client
from django.views import generic


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app/main.html'


class RegisterView(generic.CreateView):
    form_class = RegisterUser
    template_name = 'registration/register.html'

    def get_success_url(self):
        return reverse('login')


# def register(request):
#     msg = None
#     form = RegisterUser
#     if request.method == 'POST':
#         form = RegisterUser(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     return render(request, 'registration/register.html')


class List_Client(generic.ListView):
    queryset = Client.objects.all()
    template_name = 'app/list_client.html'

    def get_success_url(self):
        return reverse('success_form')


class UpdateClientView(generic.UpdateView):
    form_class = AdminClientForm
    queryset = Client.objects.all()
    context_object_name = 'client'
    template_name = 'app/update_client_document.html'

    def get_success_url(self):
        return reverse('list_client')


class UserProfileView(LoginRequiredMixin, generic.DetailView):
    queryset = Client.objects.all()
    context_object_name = 'client'
    template_name = 'app/userprofile.html'


class SendDocumentView(LoginRequiredMixin, generic.CreateView):
    form_class = ClientForm
    template_name = 'app/send_document.html'

    def form_valid(self, form):
        document = form.save(commit=False)
        document.user = self.request.user
        document.created_at = datetime.now()
        document.update_at = datetime.now()
        document.editable = False

        # document.save()
        return super(SendDocumentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('success_form')


# def send_document(request):
#     if request.method == 'POST':
#         form = ClientForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data
#             Client.objects.create(
#                 user=request.user,
#                 name=data['name'],
#                 surname=data['surname'],
#                 phone=data['phone'],
#                 passport=data['passport'],
#                 receipt_amonatbonk=data['receipt_amonatbonk']
#             )
#             return redirect('success_form')
#
#     else:
#         form = ClientForm()
#     return render(request, 'app/send_document.html', {'form': form})


# def user_profile(request, pk):
#     profile = Client.objects.get(user_id=pk)
#     return render(request, 'app/user_profile.html', {'profile': profile})


class ActiveStatusClientView(LoginRequiredMixin, generic.ListView):
    template_name = 'app/search_client.html'

    def get_queryset(self):
        client_list = None
        if self.request.user.is_superuser:
            print('q------->>')
            client_list = Client.objects.filter(status_document='Астывна')
            print('client_list', client_list)
        return client_list


class BlockStatusClientView(LoginRequiredMixin, generic.ListView):
    template_name = 'app/search_client.html'

    def get_queryset(self):
        client_list = None
        if self.request.user.is_superuser:
            print('q------->>')
            client_list = Client.objects.filter(status_document='Отменён')
            print('client_list', client_list)
        return client_list


class DoneStatusClientView(LoginRequiredMixin, generic.ListView):
    template_name = 'app/search_client.html'

    def get_queryset(self):
        client_list = None
        if self.request.user.is_superuser:
            print('q------->>')
            client_list = Client.objects.filter(status_document='Готово')
            print('client_list', client_list)
        return client_list


class SearchClientView(LoginRequiredMixin, generic.ListView):
    template_name = 'app/search_client.html'

    def get_queryset(self):
        client_list = None
        if self.request.user.is_superuser:
            query = self.request.GET.get('q')
            print('q------->>', query)
            client_list = Client.objects.filter(Q(phone__icontains=query)
                                                | Q(first_name__icontains=query)
                                                | Q(second_name__icontains=query))
            print('client_list', client_list)
        return client_list


def success_form(request):
    return render(request, 'app/success_form.html')
