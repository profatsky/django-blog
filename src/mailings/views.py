from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import SubscribeForm
from .models import Subscriber


class SubscribeToMailing(FormView):
    form_class = SubscribeForm
    template_name = 'mailings/subscribe.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        subscriber, result = Subscriber.objects.get_or_create(**form.cleaned_data)
        if result:
            send_mail(
                subject='Блог',
                message='Вы подписались на рассылку',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[subscriber.email]
            )
        return super().form_valid(form)
