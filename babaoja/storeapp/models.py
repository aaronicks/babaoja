from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(null=True, blank=True, upload_to="product_images/")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    partners = models.ManyToManyField('self',
                                    related_name='customers',
                                    symmetrical=False,
                                    blank=True
                                    )
    phone = models.CharField(max_length=15, default="Not Provided")
    address = models.CharField(max_length=150, default="Not Provided")
    city = models.CharField(max_length=100, default="Not Provided")
    state = models.CharField(max_length=100, default="Not Provided")
    zipcode = models.CharField(max_length=6, default="Not")
    country = models.CharField(max_length=100, default="Not Provided")
    profile_images = models.ImageField(null=True, blank=True, upload_to="imgs/")
    profile_bio = models.CharField(null=True, blank=True, max_length=500)
    homepage_link = models.CharField(null=True, blank=True, max_length=100)
    facebook_link = models.CharField(null=True, blank=True, max_length=100)
    instagram_link = models.CharField(null=True, blank=True, max_length=100)
    linkedin_link = models.CharField(null=True, blank=True, max_length=100)
    x_link = models.CharField(null=True, blank=True, max_length=100)
    date_modified = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} - {self.user.last_name}'
    
# automatically create profile
# @receiver(post_save, sender=User) this os the connect
def create_profile(sender, created, instance, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

        # make it follow it self
        user_profile.partners.set([instance.profile.id])
        user_profile.save()

post_save.connect(create_profile, sender=User)



class Feedback(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)  # The user giving feedback
    reviewed_user = models.ForeignKey(User, related_name="received_feedback", on_delete=models.CASCADE)  # The user receiving feedback
    feedbacks = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies")
    rating = models.IntegerField(default=1, null=True, blank=True)  # Rating from 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.reviewer} to {self.reviewed_user} - {self.rating} Stars"
