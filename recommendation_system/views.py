from django.shortcuts import render
from .forms import ReviewForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import make_recommendations

@login_required
def review(request):
    if request.method=='POST':
        u_form=ReviewForm(request.POST)
        if u_form.is_valid():
            u_form.save()
            messages.success(request,"Review Added!")
            return redirect('profile')
    else:
        u_form=ReviewForm()

    context={
        'form':u_form,
        }
    return render(request,'recommendation_system/rate.html',context)
@login_required
def recommendation(request):
    watched_movies,recc=make_recommendations.recommendations(request.user.id)
    if watched_movies==0 and recc==0:
        return render(request,'recommendation_system/gorate.html')
    else:
        return render(request,'recommendation_system/recommendation.html',{"watched_movies":watched_movies,"movie_recommendations":recc})