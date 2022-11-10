from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Health_Record


# Create your views here.
from healthcare_app.forms import MainForm


def home_view(request):
    return render(request, 'main_form.html')


def results_view(request, patient_record_id):

    patient_record = Health_Record.objects.get(id=patient_record_id)
    records = Health_Record.objects.all()
    field_names = [f.name for f in Health_Record._meta.get_fields()]

    context = {
        'patient_record': patient_record,
        'field_names': field_names,
        'records': records
    }

    return render(request, 'result_page.html', context)


def post_form(request):
    if request.method == "POST":
        rid = request.POST.get("rid")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        gender = request.POST.get('gender')
        marital_status = request.POST.get('marital_status')
        exam_date = request.POST.get('exam_date')
        cdrsb = request.POST.get('cdrsb')
        adas11 = request.POST.get('adas11')
        adas13 = request.POST.get('adas13')
        mmse = request.POST.get('mmse')
        ravlt_immediate = request.POST.get('ravlt_immediate')
        ravlt_learning = request.POST.get('ravlt_learning')
        ravlt_forgetting = request.POST.get('ravlt_forgetting')
        faq = request.POST.get('faq')
        ventricles = request.POST.get('ventricles')
        hippocampus = request.POST.get('hippocampus')
        whole_brain = request.POST.get('whole_brain')
        entorhinal = request.POST.get('entorhinal')
        fusiform = request.POST.get('fusiform')
        mid_temp = request.POST.get('mid_temp')
        icv = request.POST.get('icv')
        diagnosis = request.POST.get('diagnosis')

        data = {
            'rid': rid,
            "first_name": first_name.title(),
            "last_name": last_name.title(),
            "birth_date": birth_date,
            "gender": gender,
            "marital_status": marital_status,
            "exam_date": exam_date,
            "cdrsb": cdrsb,
            "adas11": adas11,
            "adas13": adas13,
            "mmse": mmse,
            "ravlt_immediate": ravlt_immediate,
            "ravlt_learning": ravlt_learning,
            "ravlt_forgetting": ravlt_forgetting,
            "faq": faq,
            "ventricles": ventricles,
            "hippocampus": hippocampus,
            "whole_brain": whole_brain,
            "entorhinal": entorhinal,
            "fusiform": fusiform,
            "midtemp": mid_temp,
            "icv": icv,
            "diagnosis": diagnosis
        }

        form = MainForm(data=data)
        print(form.errors)
        if form.is_valid():
            instance = form.custom_save(request.user)
            return JsonResponse({'message': 'success', 'id':instance.id})
    else:
        form = MainForm(request.POST)
        print(form.errors)
        return JsonResponse({
            'message': 'fail',
            "error": "Posting Error"
        })


