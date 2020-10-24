from django.db import models


class Customer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    emailid = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(emailid):
        try:
            return Customer.objects.get(emailid=emailid)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(emailid=self.emailid):
            return True
        else:
            return False
