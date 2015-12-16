from django.db import models

from django.core.exceptions import ValidationError

def vn(customer_name):

    if customer_name.isalpha():

        pass

    else:

        raise ValidationError('please enter alphabetics')



class detail(models.Model):

    customer_name=models.CharField(max_length=20,validators=[vn])

    customer_mnum=models.IntegerField()

    complaint_problem=models.CharField(max_length=100)

    complaint_num=models.IntegerField()


