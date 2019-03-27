from django.db import models

# Create your models here.


class Charity(models.Model):
    name = models.CharField(max_length=300)
    charity_number = models.CharField(max_length=200, blank=True)
    address_line_1 = models.CharField(max_length=400, null=True, blank=True)
    address_line_2 = models.CharField(max_length=400, null=True, blank=True)
    post_code = models.CharField(max_length=10, null=True, blank=True)
    contact_number = models.BigIntegerField(blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Charities"