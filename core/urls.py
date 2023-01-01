from django.urls import path
from .views import (
    RequestList,
    UserRequestList,
    RequestCreate,
    RequestRetrieve,
    RequestUpdate,
    RequestDestroy,
    OfferList,
    UserOfferList,
    OfferCreate,
    OfferRetrieve,
    OfferUpdate,
    OfferDestroy,
    CourseList,
    CourseRetrieve
)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('request/', RequestList.as_view(), name='RequestList'),
    path('request/user/', UserRequestList.as_view(), name='UserRequestList'),
    path('request/create/', RequestCreate.as_view(), name='RequestCreate'),
    path('request/<int:pk>/', RequestRetrieve.as_view(), name='RequestRetrieve'),
    path('request/update/<int:pk>/', RequestUpdate.as_view(), name='RequestUpdate'),
    path('request/destroy/<int:pk>/', RequestDestroy.as_view(), name='RequestDestroy'),
    path('offer/', OfferList.as_view(), name='OfferList'),
    path('offer/user/', UserOfferList.as_view(), name='UserOfferList'),
    path('offer/create/', OfferCreate.as_view(), name='OfferCreate'),
    path('offer/<int:pk>/', OfferRetrieve.as_view(), name='OfferRetrieve'),
    path('offer/update/<int:pk>/', OfferUpdate.as_view(), name='OfferUpdate'),
    path('offer/destroy/<int:pk>/', OfferDestroy.as_view(), name='OfferDestroy'),
    path('course/', CourseList.as_view(),name='CourseList'),
    path('course/<int:pk>/', CourseRetrieve.as_view(),name ='CourseRetrieve'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
