from django.shortcuts import render, redirect,get_object_or_404
from .models import Cuisine,Contact,MenuItem
from .forms import BookingForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def menu(request):
    cuisines = Cuisine.objects.all()
    return render(request, 'menu.html', {'cuisines': cuisines})

def about(request):
    return render(request, 'about.html')

def contact(request):

    if request.method == "POST":

        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )

        messages.success(
            request,
            "Your message has been sent successfully!"
        )

        return redirect('contact')

    return render(request, 'contact.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking')  # reload page
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})

def order_item(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)

    return render(request, 'order.html', {
        'item': item
    })