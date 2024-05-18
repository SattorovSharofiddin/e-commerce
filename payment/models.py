from django.db import models
from django.utils.translation import gettext_lazy as _

from orders.models import Order


class Payment(models.Model):
    PENDING = "P"
    COMPLETED = "C"
    FAILED = "F"

    STATUS_CHOICES = (
        (PENDING, _("pending")),
        (COMPLETED, _("completed")),
        (FAILED, _("failed")),
    )

    # Payment options
    PAYPAL = "P"
    PAY_BY_CARD = "PC"
    # STRIPE = "S"

    PAYMENT_CHOICES = ((PAYPAL, _("paypal")), (PAY_BY_CARD, _("pay by card")))

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    card_number = models.CharField(max_length=16, blank=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    cvv = models.CharField(max_length=4, blank=True)
    payment_option = models.CharField(max_length=2, choices=PAYMENT_CHOICES)
    order = models.OneToOneField(
        Order, related_name="payment", on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.order.buyer.get_full_name()
