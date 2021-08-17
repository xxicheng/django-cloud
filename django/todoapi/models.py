from django.db import models

from datetime import date

# Create the Task class to describe the model.
"""
#Stores a task.
title = models.CharField(max_length=50)
content = models.CharField(max_length=50)

# Date the task was created.
created_on = models.DateField(default=date.today)

# Due date.
due_date = models.DateField(default=date.today)
"""
class Task(models.Model):
    project_status = models.CharField(db_column="Project Status", max_length=50,null=True)
    project_country = models.CharField(db_column="Project Country", max_length=50,null=True)
    year = models.CharField(db_column="year", max_length=50,null=True)
    month = models.CharField(db_column="month", max_length=50,null=True)
    project_name = models.CharField(db_column="Project Name", max_length=50,null=True)
    company = models.CharField(db_column="company", max_length=50,null=True)
    project_number = models.CharField(db_column="Project Number", primary_key = True, max_length=50)
    url = models.CharField(db_column="Project URL", max_length=50,null=True)
    sector = models.CharField(db_column="Project Sector", max_length=50,null=True)
    bank = models.CharField(db_column="Project Bank", max_length=50,null=True)
    loan_amount = models.CharField(db_column="Loan Amount", max_length=50,null=True)
    currency = models.CharField(db_column="currency", max_length=50,null=True)		
    loan_amount_in_usd = models.CharField(db_column="Loan Amount in USD", max_length=50,null=True)	



    # Meta data about the database table.
    class Meta:
        # Set the table name.
        db_table = 'complaints'

        # Set default ordering
        #ordering = ['id']

    # Define what to output when the model is printed as a string.
    def __str__(self):
        return self.title
