from django.shortcuts import render
from .models import Tours
from django.shortcuts import get_object_or_404



def index(request):
    return render(request, 'catalog/index.html')

def about(request):
    return render(request, 'catalog/about.html')


def tours(request):
    title = 'туры'
    list_of_tours = Tours.objects.filter(is_active=True)

    context = {
        'title': title,
        'list_of_tours': list_of_tours,
    }

    return render(request, 'catalog/tours.html', context)


def tour(request, pk):
    title = 'тур'
    tour = get_object_or_404(Tours, pk=pk)

    context = {
        'title': title,
        'tour': tour,
    }

    return render(request, 'catalog/tour_details.html', context)
