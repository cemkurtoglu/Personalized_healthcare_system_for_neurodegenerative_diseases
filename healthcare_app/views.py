import json

from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import register
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import Health_RecordSerializer

from .models import Health_Record
from scripts import eval
# Create your views here.
from healthcare_app.forms import MainForm


def home_view(request):
    return render(request, 'home.html')


def form_view(request):
    return render(request, 'main_form.html')


def patients_view(request):
    records = Health_Record.objects.all()
    field_names = [f.name for f in Health_Record._meta.get_fields()]
    context = {
        'field_names': field_names,
        'records': records,
    }
    return render(request, 'data_base_view.html', context)


def patient_search_view(request):
    return render(request, 'patient_search.html')


def patient_record_view(request, patient_id):
    record = Health_Record.objects.get(id=patient_id)

    if record.probability and record.prediction:
        probability = record.probability * 100
        prediction = record.get_prediction()
    else:
        probability = 0
        prediction = "No Prediction Data"

    context = {
        'patient': record,
        'probability': probability,
        'prediction': prediction
    }

    return render(request, 'patient_record_profile.html', context)


def results_view(request, patient_record_id):
    patient_record = Health_Record.objects.get(id=patient_record_id)
    records = Health_Record.objects.all()
    field_names = [f.name for f in Health_Record._meta.get_fields()]

    context = {
        'patient_record': patient_record,
        'field_names': field_names,
        'records': records,
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
            "mid_temp": mid_temp,
            "icv": icv,
            "diagnosis": diagnosis
        }

        form = MainForm(data=data)
        print(form.errors)
        if form.is_valid():
            instance = form.custom_save(request.user)
            return JsonResponse({'message': 'success', 'id': instance.id})
    else:
        form = MainForm(request.POST)
        print(form.errors)
        return JsonResponse({
            'message': 'fail',
            "error": "Posting Error"
        })


# APIs

@api_view(['GET'])
def get_data(request):
    records = Health_Record.objects.all()
    serializer = Health_RecordSerializer(records, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def generate_prediction(request, patient_record_id):
    serializer = Health_RecordSerializer(data=request.data, many=True)
    if serializer.is_valid(raise_exception=True):
        output = eval.run(serializer.data)
        health_record = Health_Record.objects.get(id=patient_record_id)
        health_record.prediction = output[0]['prediction']
        health_record.probability = output[0]['probability']
        health_record.save(update_fields=["prediction", "probability"])
        return Response(output)
    return Response(serializer.data)


@api_view(['POST'])
def generate_prediction_for_all(request):
    records = Health_Record.objects.values()
    if records:
        for record in records:
            record_array = [record]
            output = eval.run(record_array)
            health_record = Health_Record.objects.get(id=record.get("id"))
            health_record.prediction = output[0]['prediction']
            health_record.probability = output[0]['probability']
            health_record.save(update_fields=["prediction", "probability"])
    return JsonResponse(serialize('json', Health_Record.objects.all()), status=201, safe=False)


class Health_RecordListView(generics.ListAPIView):
    queryset = Health_Record.objects.all()
    serializer_class = Health_RecordSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name']
