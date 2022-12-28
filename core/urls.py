from django.urls import path
from .views import RequestList, RequestDetail, OfferList, OfferDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('Request/', RequestList.as_view()),
    path('Request/<int:pk>/', RequestDetail.as_view()),
    path('Offer/', OfferList.as_view()),
    path('Offer/<int:pk>/', OfferDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
