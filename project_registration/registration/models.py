from django.db import models

# Create your models here.

class Registration(models.Model):
    ID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255,unique=True)
    DateOfBirth = models.DateField()
    Address = models.CharField(max_length=255)
    Gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])

    class Meta:
        managed = False  # Tell Django not to manage this table
        db_table = 'Registration'  # Specify the external table name
    
    def __str__(self) :
        return self.Email
