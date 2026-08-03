from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("services/", views.services, name="services"),

    path("booknow/", views.booknow, name="booknow"),

    path(
        "select-date/",
        views.select_date,
        name="select_date"
    ),

    path(
        "customer-details/",
        views.customer_details,
        name="customer_details"
    ),

    path(
        "confirm-booking/",
        views.confirm_booking,
        name="confirm_booking"
    ),

    path(
        "payment/",
        views.payment,
        name="payment"
    ),

    path(
        "about/",
        views.about,
        name="about"
    ),

    path(
        "contact/",
        views.contact,
        name="contact"
    ),
]