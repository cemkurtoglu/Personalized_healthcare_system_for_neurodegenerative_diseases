"""Personalized_healthcare_system_for_neurodegenerative_diseases URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from healthcare_app.views \
    import home_view, results_view, post_form, get_data, generate_prediction, form_view, patients_view \
    , generate_prediction_for_all, patient_record_view, Health_RecordListView, patient_search_view

app_name = 'healthcare_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('form/', form_view, name='form_view'),
    path('patients/', patients_view, name='patients_view'),
    path('patient/<int:patient_id>', patient_record_view, name='patient_record_view'),
    path('result/<int:patient_record_id>', results_view, name='results_view'),
    path('search_patient/', patient_search_view, name='patient_search_view'),
    path('api/post_form/', post_form, name='post_form'),
    path('api/get_data', get_data, name='get_data'),
    path('api/generate_prediction/<int:patient_record_id>', generate_prediction, name='generate_prediction'),
    path('api/generate_prediction_for_all', generate_prediction_for_all, name='generate_prediction_for_all'),
    path('api/search/', Health_RecordListView.as_view(), name='Health_RecordListView')



]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
