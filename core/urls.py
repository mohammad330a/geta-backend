from django.urls import path
from .views import RequestList, RequestCreate, RequestRetrieve, RequestUpdate, RequestDestroy, \
    OfferList, OfferCreate, OfferRetrieve, OfferUpdate, OfferDestroy
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('Request/', RequestList.as_view()),
    path('Request/create/', RequestCreate.as_view()),
    path('Request/<int:pk>/', RequestRetrieve.as_view()),
    path('Request/update/<int:pk>/', RequestUpdate.as_view()),
    path('Request/destroy/<int:pk>/', RequestDestroy.as_view()),
    path('Offer/', OfferList.as_view()),
    path('Offer/create/', OfferCreate.as_view()),
    path('Offer/<int:pk>/', OfferRetrieve.as_view()),
    path('Offer/update/<int:pk>/', OfferUpdate.as_view()),
    path('Offer/destroy/<int:pk>/', OfferDestroy.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
