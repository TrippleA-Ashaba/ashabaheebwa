from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils import timezone

from blog.forms import ContactForm

YEAR = timezone.now().year
# Create your views here.


def home(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f"Resume Contact: {form.cleaned_data['name']}, {form.cleaned_data['subject']}"
            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            email_from = form.cleaned_data["email"]
            email_to = "zaphod@gmail.com"
            html = render_to_string(
                "emails/contact_form.html",
                {
                    "name": name,
                    "email": email_from,
                    "subject": subject,
                    "message": message,
                    "head": "RESUME CONTACT",
                },
            )
            messages.success(request, "Email was sent Successfully!")

            send_mail(
                subject=subject,
                message=message,
                from_email=email_from,
                recipient_list=[email_to],
                html_message=html,
                fail_silently=False,
            )
            return redirect("home")
        else:
            messages.warning(request, "Something Wrong, Email was not sent!")

    return render(
        request, "resume/home.html", {"year": YEAR, "title": "contact", "form": form}
    )
