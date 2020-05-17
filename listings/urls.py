from django.urls import path
from . import views

urlpatterns=[
    # on listings/ or all lists... index of listings
    path('',views.index,name ='listings'),
    # a perticular list with id listings/id
    path('<int:listing_id>', views.listing, name = 'listing'),
    path('search',views.search,name='search'),
]