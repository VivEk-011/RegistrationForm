from django.db import models
class login(models.Model):
    login_fname = models.CharField(max_length=10)
    login_lname = models.CharField(max_length=10)
    login_email =models.EmailField(max_length=200)
    pswd = models.CharField(max_length=20)
