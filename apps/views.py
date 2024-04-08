from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.models import Product, Profile
from root.settings import EMAIL_HOST_USER


def index_menu_view(request):
    return render(request, 'apps/index.html')


def product_list_view(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'apps/product-list.html', context)


def product_detail_view(request, pk):
    context = {
        'product': Product.objects.get(pk=pk)
    }
    return render(request, 'apps/product-detail.html', context)


def send_email_view(request):
    subject = 'Welcome to My Site'
    message = 'Thank you for creating an account!'
    recipient_list = ['samariddin0304@gmail.com']
    send_mail(subject, message, EMAIL_HOST_USER, recipient_list)
    return HttpResponse('Successfully sent email!')


def form_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        Profile.objects.create(full_name=full_name, email=email, phone=phone, mobile=mobile, address=address)
    return render(request, 'apps/form.html')


def profile_detail_view(request, pk):
    profile = Profile.objects.get(pk=pk)

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        profile.full_name = full_name
        profile.email = email
        profile.phone = phone
        profile.mobile = mobile
        profile.address = address
        profile.save()
        return redirect('index_menu_view')

    context = {
        'profile': profile
    }
    return render(request, 'apps/form.html', context)

# product(name, price, description)


# https://bootdey.com/snippets/view/profile-edit-data-and-skills
