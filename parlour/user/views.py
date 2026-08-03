from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")

def booknow(request):

    if request.method == "POST":

        selected_service = request.POST.get("service")

        return render(
            request,
            "booknow.html",
            {
                "selected_service": selected_service
            }
        )

    return render(request, "booknow.html")

def bookdate(request):
    if request.method == "POST":
        selected_date = request.POST.get("date")
        selected_time = request.POST.get("time")

        return render(
            request,
            "bookdate.html",
            {
                "selected_date": selected_date,
                "selected_time": selected_time
            }
        )

    return render(request, "bookdate.html")