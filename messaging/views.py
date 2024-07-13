from django.shortcuts import HttpResponse
from django.core.mail import EmailMessage
from messaging.tasks import log_message


def send_mail(request):
    email = request.GET.get('sendmail')
    talktome = request.GET.get('talktome', False)  # Default talktome to False

    if email:
        # Use EmailMessage with your SMTP details
        message = EmailMessage(
            'Messaging System with Celery/RabbitMQ',
            'This is a test email for HNG DevOps stage 3',
            'boluwatifetella@gmail.com',
            [email],
        )

        message.send(fail_silently=False)

    if talktome:
        log_message("Message sent")

    response = "Email sent" if email else ""
    response += " and message logged" if talktome else ""
    return HttpResponse(response or "No actions performed.")
