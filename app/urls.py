from .views import (HomeView, RegisterView, success_form, SendDocumentView, \
                    List_Client, UpdateClientView, UserProfileView, SearchClientView,
                    ActiveStatusClientView, BlockStatusClientView, DoneStatusClientView)
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/register', RegisterView.as_view(), name='register'),
    path('user/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('document/', SendDocumentView.as_view(), name='send_document'),
    path('success_form/', success_form, name='success_form'),
    path('list-client/', List_Client.as_view(), name='list_client'),
    path('client/<int:pk>/', UpdateClientView.as_view(), name='detail_client'),
    path('search_client/', SearchClientView.as_view(), name='search_client'),
    path('active_status/', ActiveStatusClientView.as_view(), name='active_status_client'),
    path('block_status/', BlockStatusClientView.as_view(), name='block_status_client'),
    path('done_status/', DoneStatusClientView.as_view(), name='done_status_client')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
