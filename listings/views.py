from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator

from listings.choices import state_choices,bedroom_choices,price_choices

from .models import Listing



def index(request):
    # SQL query with ORM 
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)
    
    paginator = Paginator(listings, 2)
    page_number = request.GET.get('page')
    # page object 
    paged_listings = paginator.get_page(page_number)
    
    # dictionary for templete
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/index_listings.html',context)

# single listing
def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk = listing_id)

    context = {
        'listing' : listing
    }

    return render(request, 'listings/listing.html',context)

def search(request):
    queryset_list = Listing.objects.all()

  # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(discription__icontains=keywords)
    

        # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__icontains=city)

  # State
    # elif 'state' in request.GET:
    #     state = request.GET['state']
    #     if state:
    #         queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
    # if 'bedroom' in request.GET:
    #     bedroom = request.GET['bedroom']
    #     if bedroom:
    #         queryset_list = queryset_list.filter(bedroom__gte=bedroom)

  # Price
    # if 'price' in request.GET:
    #     price = request.GET['price']
    #     if price:
    #         queryset_list = queryset_list.filter(price__lte=price)

    context ={
        'listings' : queryset_list,
        'state_choices' : state_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,
    }
    return render(request, 'listings/search.html',context)