from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Profile
import json


# -------------------------
# Dashboard (main page)
# -------------------------
def dashboard(request):
    return render(request, 'dashboard.html')


# -------------------------
# Signup API
# -------------------------

@csrf_exempt
@csrf_exempt
def signup(request):
    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return JsonResponse({"error": "Missing fields"}, status=400)

        if User.objects.filter(username=email).exists():
            return JsonResponse({"error": "User already exists"}, status=400)

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        auth_login(request, user)

        return JsonResponse({"success": True})

    return JsonResponse({"error": "Invalid request"}, status=400)

# -------------------------
# Login API
# -------------------------
@csrf_exempt
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        print("LOGIN ATTEMPT:", email, password)

        user = authenticate(request, username=email, password=password)

        print("AUTH RESULT:", user)

        if user is not None:
            auth_login(request, user)
            return JsonResponse({"success": True})

        return JsonResponse({"success": False})

    return JsonResponse({"error": "Invalid request"}, status=400)

# -------------------------
# Buy/Sell Section
# -------------------------
#@login_required(login_url='signin')
def buy_sell_home(request):
    return render(request, 'buy_sell_home.html')

#@login_required(login_url='signin')
def buy(request):
    return render(request, 'buy.html')

#@login_required(login_url='signin')
def sell(request):
    return render(request, 'sell.html')


# -------------------------
# Stray Dog Section
# -------------------------
@login_required(login_url='signin')
def straydog_report_home(request):
    return render(request, 'straydog_report_home.html')

@login_required(login_url='signin')
def straydog_reporter(request):
    return render(request, 'straydog_reporter.html')
def check_auth(request):
    return JsonResponse({
        "authenticated": request.user.is_authenticated
    })