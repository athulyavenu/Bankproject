from django.db import models


class District(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(choices = (('Male','Male'), ('Female','Female'),('Does not wish to specify','Does not wish to specify')), max_length=50)
    phone_num = models.CharField(max_length=13)
    mail_id = models.EmailField()
    address = models.TextField(max_length=250)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    accounttype = models.CharField(choices = (('Savings Account','Savings Account'), ('Current Account','Current Account'),('Demat Account','Demat Account')), max_length=20)
    creditcard = models.BooleanField(default=False)
    debitcard = models.BooleanField(default=False)

    def __str__(self):
        return self.name