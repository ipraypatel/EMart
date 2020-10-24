from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from Store.models.customer import Customer
from django.views import View

class Signup(View):
    def validateCustomer(self, customer):
        error_message = None
        if (not customer.fname):
            error_message = "First Name Required!"
        elif len(customer.fname) < 4:
            error_message = 'Enter Valid First Name!'
        elif not customer.lname:
            error_message = 'Last Name Required!'
        elif len(customer.lname) < 4:
            error_message = 'Enter Valid Last Name!'
        elif not customer.phone:
            error_message = 'Phone Number Required!'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be of 10 Digits!'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 Characters Long!'
        elif customer.isExists():
            error_message = 'Email Address is Already Registered!'
        return error_message

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        post_data = request.POST
        fname = post_data.get('fname')
        lname = post_data.get('lname')
        phone = post_data.get('phone')
        emailid = post_data.get('emailid')
        password = post_data.get('password')

        # validations
        value = {
            'fname': fname,
            'lname': lname,
            'phone': phone,
            'emailid': emailid
        }

        error_message = None

        customer = Customer(fname=fname,
                            lname=lname,
                            phone=phone,
                            emailid=emailid,
                            password=password)
        error_message = self.validateCustomer(customer)

        # saving
        if not error_message:

            print(fname, lname, phone, emailid, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
