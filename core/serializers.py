from rest_framework import serializers
from .models import Request, Offer


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'student', 'course', 'telegram_id', 'email', 'description')


class CreateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'course', 'telegram_id', 'email', 'description')


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'instructor', 'course', 'telegram_id', 'email', 'description')


class CreateOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'course', 'telegram_id', 'email', 'description')
