from django.shortcuts import render
from .forms import ReviewForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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