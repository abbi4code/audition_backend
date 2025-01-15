from django.db import models
import os


def audition_image_path(instance_id, filename):
    return os.path.join('ArhnLogo', str(instance_id), filename)


class AuditionPortal(models.Model):
    name = models.CharField(max_length=200, blank=False)
    roll_no = models.CharField(max_length=50, blank=False, null=True)
    contact_number = models.CharField(max_length=10, blank=False, unique=True)
    email = models.EmailField(unique=True, blank=False)
    department = models.CharField(max_length=200, blank=False, null=True)

    def __str__(self):
        return str(self.name)

class DesignWorkshop(models.Model):
    name = models.CharField(max_length=200, blank=False)
    roll_no = models.CharField(max_length=50, blank=False, null=True)
    contact_number = models.CharField(max_length=10, blank=False, unique=True)
    email = models.EmailField(unique=True, blank=False)
    department = models.CharField(max_length=200, blank=False, null=True)
    year = models.CharField(max_length=200, blank=False, null=True)
    payment_proof=models.ImageField(upload_to="payment_images/", blank=True, null=True)

    def __str__(self):
        return str(self.name)

class ValorantGaming(models.Model):
    name = models.CharField(max_length=200, blank=False)
    contact_number = models.CharField(max_length=10, blank=False, unique=True)
    email = models.EmailField(unique=True, blank=False)
    payment_proof=models.ImageField(upload_to="valo_payment_images/", blank=True, null=True)

    def __str__(self):
        return str(self.name)


class BgmiGaming(models.Model):
    name = models.CharField(max_length=200, blank=False)
    contact_number = models.CharField(max_length=10, blank=False, unique=True)
    email = models.EmailField(unique=True, blank=False)
    payment_proof=models.ImageField(upload_to="bgmi_payment_images/", blank=True, null=True)

    def __str__(self):
        return str(self.name)
