from django.db import models


class Contestant(models.Model):
    solver_id = models.CharField(max_length=10, primary_key=True, db_column='Solver ID')
    first_name = models.CharField(max_length=20, db_column='First Name')
    last_name = models.CharField(max_length=20, db_column='Last Name')
    username = models.CharField(max_length=10, db_column='Username')
    password = models.CharField(max_length=20, db_column='Password')
    email = models.EmailField(max_length=30, db_column='Email')

    class Meta:
        db_table = "Contestant"