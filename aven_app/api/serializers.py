from rest_framework import serializers
from app.models import Appointment, Contact

#*IMPORTANT: SERIALIZER MODEL APPOINTMENT
class AppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ("firstName", "lastName", "email", "phoneNumber", "selectTimeList", "budget", "created_at", "updated_at",)
        read_only_fields = ("created_at", "updated_at",)
        
#*IMPORTANT: SERIALIZER MODEL CONTACT
class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("titleReview", "address", "firstName", "lastName", "email", "phoneNumber", "content", "user_published", "created_at", "updated_at",)
        read_only_fields = ("created_at", "updated_at",)