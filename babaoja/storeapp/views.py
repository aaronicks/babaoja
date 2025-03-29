from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile, Product, Feedback
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, ProfilePicForm
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    products = Product.objects.select_related('user__profile').order_by("?")
    return render(request, 'home.html', {'products': products,})



def my_profile(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user_id=request.user.id)
        products = Product.objects.filter(user_id=request.user.id)
        
    else:
        messages.error(request, 'You need to log in to be able to view the profile')
        return redirect('user_login')
    return render(request, 'my_profile.html', {'profile': profile, 'products':products})



def user_profile(request, pk):
    if request.user.is_authenticated:
        # profile = profile = Profile.objects.prefetch_related("partners").get(user_id=pk)
        profile = get_object_or_404(Profile, user_id=pk)
        products = Product.objects.filter(user_id=pk)
        if products:
            for product in products:
                user_product = product
        else:
            messages.warning(request, 'There not posted product yet')
            return redirect('home')
        
        
        # Retrieve feebacks
        # get user id
        user_id = get_object_or_404(User, pk=pk)
        # use it to filter the feeback that belongs to the user
        feedbacks = Feedback.objects.filter(reviewed_user=user_id).order_by('-created_at')
    else:
        messages.error(request, 'You need to log in to be able to view the profile')
        return redirect('user_login')
    
    context = {
        'profile': profile, 
        'products': products, 
        'user_product': user_product,
        'feedbacks': feedbacks,
        }
    
    return render(request, 'user_profile.html', context)


def feedback(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in before you can give feedback.")
        return redirect("user_login")  # Redirect to login page

    if request.method == "POST":
        reviewed_user = get_object_or_404(User, id=pk)
        feedback_text = request.POST.get("feedback")

        if not feedback_text:
            messages.error(request, "No feedback to send.")
            return redirect("user_profile", pk=reviewed_user.id)

        # Create feedback
        Feedback.objects.create(
            reviewer=request.user,
            reviewed_user=reviewed_user,
            feedbacks=feedback_text
        )

        messages.success(request, "Your feedback has been submitted.")
        return redirect("user_profile", pk=reviewed_user.id)  # Ensure `pk` is correctly used

    return redirect("user_profile", pk=pk)




def feedback_reply(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in before you can give feedback.")
        return redirect("user_login")
    
    feedback = get_object_or_404(Feedback, id=pk)
    profile = Profile.objects.filter(user=feedback.reviewed_user).first()

    if not profile:
        messages.error(request, "The user's profile does not exist.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))  # Redirect to a safe page

    if request.method == "POST":
        reply_feedback = request.POST.get("reply")

        if not reply_feedback:
            messages.error(request, "Reply cannot be empty.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        # Create reply as a child feedback
        Feedback.objects.create(
            reviewer=request.user,
            reviewed_user=feedback.reviewed_user,
            feedbacks=reply_feedback,  # Ensure correct field name
            parent=feedback,  
        )
        messages.success(request, "Reply added successfully!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))




def product_list(request, pk):
    if request.user.is_authenticated:
        products = Product.objects.filter(user_id=pk)
    else:
        messages.error(request, 'Your need to log in to access that page')
        return redirect('user_login')
    return render(request, 'product_list.html', {'products': products})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # autheticate the info
        user = authenticate(request, username=username, password=password)

        # check if info is correct
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invlid Credentials. Please try again later')
            return redirect('home')

    return render(request, 'user_login.html', {})

def user_logout(request):
    logout(request)
    messages.success(request, 'you Have successfully logged out')
    return redirect('home')






def user_signup(request):
    form  = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()

            # extract clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # use the clean date to authenticate
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Registered Successfully')
            return redirect('home')
        
        # if form is not valid
        return render(request, 'user_signup.html', {'form': form})

    # request is Get render the empty form
    return render(request, 'user_signup.html', {'form': form})



def update_user(request):
    if request.user.is_authenticated:
        # Get the current user and profile
        current_user = get_object_or_404(User, id=request.user.id)
        user_profile, created = Profile.objects.get_or_create(user_id=request.user.id)
        print

        form = SignUpForm(request.POST or None, request.FILES or None, instance=current_user)
        img_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=user_profile)

        if form.is_valid() and img_form.is_valid():
            form.save()
            img_form.save()
            messages.success(request, 'User Updated Successfully')
            return redirect('home')

        return render(request, 'update_user.html', {'form': form, 'img_form': img_form})

    else:
        messages.error(request, 'You must be logged in to view that page.')
        return redirect('user_login')  # Ensure 'user_login' matches your URL names
    



def product_detail(request, pk):
    return render(request, 'product_detail.html', {})
