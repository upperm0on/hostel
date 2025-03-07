from django.shortcuts import render, redirect
from .models import Reviews
from consumers.models import Consumer
from ratings.models import five_star, four_star, three_star, two_star, one_star

# Create your views here.

def create_review(request):
    if request.method == 'POST':
        user = request.user
        hostel = Consumer.objects.get(user=user).hostel
        review = request.POST.get('review')

        rating = request.POST.get('rating')
        rating_dict = {
            '1': one_star,
            '2': two_star,
            '3': three_star,
            '4': four_star,
            '5': five_star
        }

        rating_dict[rating].objects.create(product=hostel).save()
        
        review = Reviews(user=user, hostel=hostel, review=review, rating=rating)
        review.save()
    return redirect('dashboard')
