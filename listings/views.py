from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator

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
    return render(request, 'listings/search.html')