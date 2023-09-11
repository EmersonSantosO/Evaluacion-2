"""
URL configuration for helpdesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tickets.views import TicketsList, EspecialidadCreate, SoporteTICreate, TicketsCreate, TicketsUpdate, TicketsDelete, TicketsDetail
from django.conf.urls.static import static 
from django.conf import settings 
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tickets_list/', TicketsList.as_view(), name = 'tickets_list'),
    path('especialidad_form/', EspecialidadCreate.as_view(), name = 'especialidadti_form'),
    path('soporteti_form/', SoporteTICreate.as_view(), name = 'soporteti_form'),
    path('tickets_form/', TicketsCreate.as_view(), name = 'tickets_form'),
    path('tickets_detail/<str:pk>', TicketsDetail.as_view(), name = 'tickets_detail'),
    path('tickets_update_form/<str:pk>', TicketsUpdate.as_view(), name = 'tickets_update_form'),
    path('tickets_delete/<str:pk>', TicketsDelete.as_view(), name = 'tickets_confirm_delete'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)