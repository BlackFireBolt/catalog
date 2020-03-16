from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Task to send an email notification when an order is
    successfully created
    """
    order = Order.objects.get(id=order_id)
    subject = 'Заказ номер {}'.format(order.id)
    message = 'Уважаемый {}, \n\nВы успешно оформили заказ.\nВаш номер заказа - {}'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message, 'admin@catalog.com', [order.email])
    return mail_sent
