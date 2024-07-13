from django.shortcuts import HttpResponse
from django.core.mail import EmailMessage
from messaging.tasks import log_message
import os


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

    response = "Email queued for sending to '{}'".format(
        email) if email else ""
    response += " and message logged" if talktome else ""
    return HttpResponse(response or "No actions performed.")


def get_logs(request):
    try:
        with open('../devops-stage3/var/log/messaging_system.log', 'r') as f:
            logs = f.read()
        return HttpResponse(logs, content_type='text/plain; charset=utf-8')
    except Exception as e:
        return HttpResponse(f"Failed to retrieve logs: {str(e)}", status=500)
