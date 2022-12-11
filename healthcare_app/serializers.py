from rest_framework import serializers

from healthcare_app.models import Health_Record


class Health_RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health_Record
        fields = "__all__"
