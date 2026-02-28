from django.urls import path
from . import views  # import all views from views.py
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Authentication
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="signin"),


    # Dashboard (main page after login)
    path("", views.dashboard, name="dashboard"),

    # Buy/Sell Section
    path("buy-sell/", views.buy_sell_home, name="buy_sell_home"),
    path("buy-sell/buy.html", views.buy, name="buy"),
    path("buy-sell/sell.html/", views.sell, name="sell"),

    # Stray Dog Section
    path("report-incident.html/", views.straydog_report_home, name="straydog_report_home"),
    path("report-incident.html/report.html", views.straydog_reporter, name="straydog_reporter"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)