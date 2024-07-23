from django.db import models


class Contact(models.Model):
    ISPIN = 'ISPIN'
    SCAI = 'SCAI'
    BOTH = 'Both'
    PRODUCT_CHOICES = [
        (ISPIN, 'ISPIN'),
        (SCAI, 'SCAI'),
        (BOTH, 'Both'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    product_interested = models.CharField(
        max_length=5, choices=PRODUCT_CHOICES, default=ISPIN)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
