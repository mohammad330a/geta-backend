from .models import Request, Offer
from .serializers import RequestSerializer, OfferSerializer
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from accounts.models import User



class RequestList(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestCreate(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticated, )

    # def perform_create(self, serializer):
    #     student = get_object_or_404(User, id=self.request.data.get('username'))
    #     return serializer.save(student=student)


class RequestRetrieve(generics.RetrieveAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestUpdate(generics.UpdateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticated, )


class RequestDestroy(generics.DestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticated, )


class OfferList(generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class OfferCreate(generics.CreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (permissions.IsAuthenticated, )


class OfferRetrieve(generics.RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class OfferUpdate(generics.UpdateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (permissions.IsAuthenticated, )


class OfferDestroy(generics.DestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (permissions.IsAuthenticated, )
