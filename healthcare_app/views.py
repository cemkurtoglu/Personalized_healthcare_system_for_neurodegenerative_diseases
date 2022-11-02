from django.http import HttpResponse
from django.shortcuts import render
from .models import Health_Record


# Create your views here.
from healthcare_app.forms import MainForm


def home_view(request):
    return render(request, 'main_form.html')


def post_form(request):
    if request.method == "POST":
        print("\n-------------------\n")
        main_form = MainForm(request.POST)
        if main_form.is_valid():
            main_form.save(commit=True)
            print("Printing post: ", request.POST)
            main_form = MainForm()
            return HttpResponse("Success")
        else:
            print(main_form.errors)


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
