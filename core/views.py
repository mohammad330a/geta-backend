from rest_framework import generics, permissions
from .models import Request, Offer, Course
from .serializers import RequestSerializer, OfferSerializer,\
    UserRequestSerializer, UserOfferSerializer, CourseSerializer


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieve(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RequestList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class UserRequestList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = RequestSerializer

    def get_queryset(self):
        return Request.objects.filter(student=self.request.user)


class RequestCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Request.objects.all()
    serializer_class = UserRequestSerializer

    def perform_create(self, serializer):
        return serializer.save(student=self.request.user)


class RequestRetrieve(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestUpdate(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Request.objects.all()
    serializer_class = UserRequestSerializer

    def perform_create(self, serializer):
        return serializer.save(student=self.request.user)


class RequestDestroy(generics.DestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = Request.objects.all()
    serializer_class = UserRequestSerializer

    def perform_create(self, serializer):
        return serializer.save(student=self.request.user)


class OfferList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class UserOfferList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Offer.objects.all()
    serializer_class = UserOfferSerializer

    def get_queryset(self):
        return Offer.objects.filter(instructor=self.request.user)


class OfferCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Offer.objects.all()
    serializer_class = UserOfferSerializer

    def perform_create(self, serializer):
        return serializer.save(instructor=self.request.user)


class OfferRetrieve(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class OfferUpdate(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Offer.objects.all()
    serializer_class = UserOfferSerializer

    def perform_create(self, serializer):
        return serializer.save(instructor=self.request.user)


class OfferDestroy(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Offer.objects.all()
    serializer_class = UserOfferSerializer

    def perform_create(self, serializer):
        return serializer.save(instructor=self.request.user)
