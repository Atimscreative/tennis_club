from django.db import models



# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11, null=True)
    joined_at = models.DateTimeField(auto_now_add=True, null=True)

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
