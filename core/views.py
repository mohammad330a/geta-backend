from .models import Request, Offer
from .serializers import RequestSerializer, OfferSerializer, CreateRequestSerializer
from rest_framework import generics, permissions


class RequestList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = RequestSerializer

    def get_queryset(self):
        return Request.objects.filter(student=self.request.user)


class RequestCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Request.objects.all()
    serializer_class = CreateRequestSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(student=self.request.user)


class RequestRetrieve(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestUpdate(generics.UpdateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticated, )


class RequestDestroy(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class OfferList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get_queryset(self):
        return Offer.objects.filter(instructor=self.request.user)


class OfferCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(instructor=self.request.user)


class OfferRetrieve(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class OfferUpdate(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (permissions.IsAuthenticated, )


class OfferDestroy(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (permissions.IsAuthenticated, )
