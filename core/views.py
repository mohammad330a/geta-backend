from .models import Request, Offer
from .serializers import RequestSerializer, OfferSerializer
from rest_framework import generics, permissions


class RequestList(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticated, )


class OfferList(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class OfferDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (permissions.IsAuthenticated, )

