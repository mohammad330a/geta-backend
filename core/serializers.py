from rest_framework import serializers
from .models import Request, Offer, Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='student.username')

    class Meta:
        model = Request
        fields = ('id', 'student', 'topic', 'course', 'telegram_id', 'email', 'description', 'created', 'username')


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'course', 'telegram_id', 'email', 'description')


class OfferSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='instructor.username')

    class Meta:
        model = Offer
        fields = ('id', 'instructor', 'topic', 'course', 'telegram_id', 'email', 'description', 'created', 'username')


class UserOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'course', 'telegram_id', 'email', 'description')
