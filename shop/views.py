from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileEditForm, UserEditForm
from .models import Profile
from igdb_api_python.igdb import igdb
from twitch import TwitchClient
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer

igdb = igdb("d1299d9ef9359fa3d5dcc112abf4b956")
#igdb = igdb("03af7252c1029ac5f2235e4d92e9ab4d")


def home(request):
    return render(request, 'shop/home.html',
                 {'home': home})


def about(request):
    return render(request, 'shop/about.html', {})


def contact(request):
    return render(request, 'shop/contact.html', {})

@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()

    #Overwatch (8713), RDR2 (25076), God of War (19560), BOTW (7346), Fortnite (1905)
    result = igdb.games({
        'ids': [8173, 25076, 19560, 7346, 1905],
        'fields': ['name', 'summary']
    })

    #overwatch dumps / loads
    ov_name_d = json.dumps(result.body[0]['name'])
    ov_name_l = json.loads(ov_name_d)
    ov_sum_d = json.dumps(result.body[0]['summary'])
    ov_sum_l = json.loads(ov_sum_d)
    ov_date = 'May 24 2016'


    #RDR2 dumps / loads
    rdr_name_d = json.dumps(result.body[1]['name'])
    rdr_name_l = json.loads(rdr_name_d)
    rdr_sum_d = json.dumps(result.body[1]['summary'])
    rdr_sum_l = json.loads(rdr_sum_d)
    rdr_date = "October 26th 2018"


    #GOW dumps / loads
    gow_name_d = json.dumps(result.body[2]['name'])
    gow_name_l = json.loads(gow_name_d)
    gow_sum_d = json.dumps(result.body[2]['summary'])
    gow_sum_l = json.loads(gow_sum_d)
    gow_date = "April 20th 2018"

    # BOTW dumps / loads

    botw_name_d = json.dumps(result.body[3]['name'])
    botw_name_l = json.loads(botw_name_d)
    botw_sum_d = json.dumps(result.body[3]['summary'])
    botw_sum_l = json.loads(botw_sum_d)
    botw_date = "March 3rd 2017"


    # Fortnite dumps / loads

    fort_name_d = json.dumps(result.body[4]['name'])
    fort_name_l = json.loads(fort_name_d)
    fort_sum_d = json.dumps(result.body[4]['summary'])
    fort_sum_l = json.loads(fort_sum_d)
    fort_date = "July 25 2017"

    #if statements

    if slug == 'fortnite':
        name = fort_name_l
        summary = fort_sum_l
        rel_date = fort_date
    elif slug == 'god-war':
        name = gow_name_l
        summary = gow_sum_l
        rel_date = gow_date
    elif slug == 'overwatch':
        name = ov_name_l
        summary = ov_sum_l
        rel_date = ov_date
    elif slug == 'red-dead-redemption-2':
        name = rdr_name_l
        summary = rdr_sum_l
        rel_date = rdr_date
    elif slug == 'zelda-breath-wild':
        name = botw_name_l
        summary = botw_sum_l
        rel_date = botw_date
    else:
        name = 'ERROR'
        summary = 'ERROR'
        rel_date = 'ERROR'

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'name': name,
                   'summary': summary,
                   'rel_date': rel_date
                   })


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'shop/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'shop/register.html',
                  {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'shop/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


class ProductList(APIView):

    def get(self,request):
        products_json = Product.objects.all()
        serializer = ProductSerializer(products_json, many=True)
        return Response(serializer.data)

