from django.test import TestCase
from datetime import datetime


# Create your tests here.



start_date = '2002-01-01'
fmt = '%Y-%m-%d'

new_date = datetime.strptime(start_date, fmt)
todate = datetime.now()


