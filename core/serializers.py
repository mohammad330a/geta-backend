from rest_framework import serializers
from .models import Request, Offer, Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'course', 'telegram_id', 'email', 'description')


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class UserOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'course', 'telegram_id', 'email', 'description')
