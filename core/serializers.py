from rest_framework import serializers
from .models import Request, Offer


# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('student', 'course', 'telegram_id', 'email', 'description')


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('student', 'course', 'telegram_id', 'email', 'description')
