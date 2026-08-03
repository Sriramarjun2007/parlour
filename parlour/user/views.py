from django.shortcuts import render, redirect


def home(request):
    return render(request, "home.html")


def services(request):
    return render(request, "services.html")


# ================= BOOK NOW =================

def booknow(request):

    if request.method == "POST":

        service = request.POST.get("service")

        if service:
            request.session["service"] = service
            return redirect("select_date")

    return render(request, "booknow.html")


# ================= SELECT DATE =================

def select_date(request):

    service = request.session.get("service")

    if not service:
        return redirect("booknow")

    prices = {
        "Haircut": 50,
        "Manicure": 30,
        "Pedicure": 40,
        "Facial": 70,
    }

    price = prices.get(service, 0)

    if request.method == "POST":

        booking_date = request.POST.get("booking_date")

        if not booking_date:

            return render(
                request,
                "select_date.html",
                {
                    "service": service,
                    "price": price,
                }
            )

        request.session["booking_date"] = booking_date
        request.session["price"] = price

        # Go to customer details page
        return redirect("customer_details")

    return render(
        request,
        "select_date.html",
        {
            "service": service,
            "price": price,
        }
    )


# ================= CUSTOMER DETAILS =================

def customer_details(request):

    service = request.session.get("service")
    booking_date = request.session.get("booking_date")
    price = request.session.get("price")

    if not service or not booking_date:
        return redirect("booknow")

    if request.method == "POST":

        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        notes = request.POST.get("notes")

        # Required fields
        if not name or not mobile:

            return render(
                request,
                "customer_details.html",
                {
                    "service": service,
                    "booking_date": booking_date,
                    "price": price,
                    "error": "Please enter your name and mobile number."
                }
            )

        # Save customer information
        request.session["customer_name"] = name
        request.session["customer_mobile"] = mobile
        request.session["customer_notes"] = notes

        return redirect("confirm_booking")

    return render(
        request,
        "customer_details.html",
        {
            "service": service,
            "booking_date": booking_date,
            "price": price,
        }
    )


# ================= CONFIRM BOOKING =================

def confirm_booking(request):

    service = request.session.get("service")
    booking_date = request.session.get("booking_date")
    price = request.session.get("price")

    name = request.session.get("customer_name")
    mobile = request.session.get("customer_mobile")
    notes = request.session.get("customer_notes")

    if not service or not booking_date:
        return redirect("booknow")

    if not name or not mobile:
        return redirect("customer_details")

    context = {
        "service": service,
        "booking_date": booking_date,
        "price": price,
        "name": name,
        "mobile": mobile,
        "notes": notes,
    }

    return render(
        request,
        "confirm_booking.html",
        context
    )


# ================= PAYMENT =================

def payment(request):

    service = request.session.get("service")
    booking_date = request.session.get("booking_date")
    price = request.session.get("price")

    name = request.session.get("customer_name")
    mobile = request.session.get("customer_mobile")
    notes = request.session.get("customer_notes")

    context = {
        "service": service,
        "booking_date": booking_date,
        "price": price,
        "name": name,
        "mobile": mobile,
        "notes": notes,
    }

    return render(
        request,
        "payment.html",
        context
    )


# ================= ABOUT =================

def about(request):
    return render(request, "about.html")


# ================= CONTACT =================

def contact(request):
    return render(request, "contact.html")