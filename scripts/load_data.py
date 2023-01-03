from healthcare_app.models import Health_Record
import csv


def run():
    with open('static/data.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Health_Record.objects.all().delete()

        for row in reader:
            print(row)

            date = row[1]
            day = date.split('.')[0]
            month = date.split('.')[1]
            year = date.split('.')[2]
            new_date = year + '-' + month + '-' + day

            record = Health_Record(rid=row[0],
                                   first_name='John',
                                   last_name='Doe',
                                   exam_date=new_date,
                                   gender=row[2],
                                   marital_status=row[3],
                                   cdrsb=row[5],
                                   adas11=row[6],
                                   adas13=row[7],
                                   mmse=row[8],
                                   ravlt_immediate=row[9],
                                   ravlt_learning=row[10],
                                   ravlt_forgetting=row[11],
                                   faq=row[12],
                                   ventricles=row[13],
                                   hippocampus=row[14],
                                   whole_brain=row[15],
                                   entorhinal=row[16],
                                   fusiform=row[17],
                                   mid_temp=row[18],
                                   icv=row[19],
                                   diagnosis=row[20])
            record.save()
