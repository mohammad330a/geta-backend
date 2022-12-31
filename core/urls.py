from django.urls import path
from .views import RequestList, UserRequestList, RequestCreate, RequestRetrieve, RequestUpdate, RequestDestroy, \
    OfferList, UserOfferList, OfferCreate, OfferRetrieve, OfferUpdate, OfferDestroy
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('request/', RequestList.as_view()),
    path('request/user/', UserRequestList.as_view()),
    path('request/create/', RequestCreate.as_view()),
    path('request/<int:pk>/', RequestRetrieve.as_view()),
    path('request/update/<int:pk>/', RequestUpdate.as_view()),
    path('request/destroy/<int:pk>/', RequestDestroy.as_view()),
    path('offer/', OfferList.as_view()),
    path('offer/user/', UserOfferList.as_view()),
    path('offer/create/', OfferCreate.as_view()),
    path('offer/<int:pk>/', OfferRetrieve.as_view()),
    path('offer/update/<int:pk>/', OfferUpdate.as_view()),
    path('offer/destroy/<int:pk>/', OfferDestroy.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
