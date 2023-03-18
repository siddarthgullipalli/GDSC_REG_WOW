from django.db import models
import uuid



class student(models.Model):
    # id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    # user_id = models.CharField(max_length=100,default = uuid.uuid4)
    # id  = models.CharField( max_length = 228 , primary_key=True)
    # id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=228 )
    last_name = models.CharField(max_length=228 )
    ph_number = models.IntegerField()
    email = models.CharField(max_length=228 )
    college = models.CharField(max_length=228 )
    branch = models.CharField(max_length=228)
    member = models.BooleanField(default=False)
    address = models.TextField(null = True , blank = True)
    img = models.ImageField(upload_to='images/')





    
