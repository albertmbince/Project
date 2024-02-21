from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from App.models import*
from .forms import AddToCartForm
from .forms import FeedbackForm






def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def view_cart(request):
    return render(request,'view_cart.html')
@login_required (login_url='login/')
def place_order(request):
    return render(request,'checkout.html')

@login_required (login_url='login/')
def second(request):
    return render(request,'second.html')
def anime(request):
    return render(request,'anime.html')
def anime2(request):
    return render(request,'anime2.html')
def anime3(request):
    return render(request,'anime3.html')
def details(request):
    return render(request,'details.html')
def checkout(request):
    return render(request, 'checkout.html')
def contact(request):
    return render(request, 'contact.html')




def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('cpass1')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                    messages.info(request,'username already exists')
                    print("Already Have")
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                print('success')
                return redirect(user_login)
        else:
            print("wrong password")
    return render(request,'signup.html')
def user_login(request):
    if request.method=='POST':
        Username=request.POST.get('username')
        password1=request.POST.get('pass1')
        user=authenticate(request,username=Username,password=password1)
        if user is not None:
            login(request,user)
            return redirect(second)
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect(user_login)
    return render(request,'login.html')
        

def user_logout(request):
    logout(request)
    return redirect(user_login)
def list(request):
    content=Vehicle.objects.all()
    data={
        'result':content
    }
    return render(request,'list.html',data)

def acessories(request):
    content=Spare.objects.all()
    data={
        'Data':content
    }
    return render(request,'spare.html',data)

def places(request,place):
    vehicles_in_place = Vehicle.objects.filter(place=place)
    data = {
        'Vplace': vehicles_in_place,
    }
    return render(request, 'places.html',data)

def types(request,type):
    spares_of_type = Spare.objects.filter(type=type)
    data = {
        'Ttype': spares_of_type,
    }
    return render(request, 'types.html',data)




@login_required
def wishlist(request):
    user = request.user
    wishlist_items = WishlistItem.objects.filter(user=user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, vehicle_id):
    user = request.user
    vehicle = Vehicle.objects.get(id=vehicle_id)
    wishlist_item = WishlistItem(user=user, vehicle=vehicle)
    wishlist_item.save()
    return redirect('wishlist')

@login_required
def remove_from_wishlist(request, wishlist_item_id):
    WishlistItem.objects.get(pk=wishlist_item_id).delete()
    return redirect('wishlist')

@login_required
def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.spare.price * item.quantity for item in cart_items)
    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, spare_id):
    user = request.user
    spare = Spare.objects.get(id=spare_id)
    cart_item = CartItem(user=user, spare=spare)
    cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, cart_item_id):
    CartItem.objects.get(pk=cart_item_id).delete()
    return redirect('view_cart')

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_feedback')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def view_feedback(request):
    feedback_list = Feedback.objects.all()
    return render(request, 'view_feedback.html', {'feedback_list': feedback_list})