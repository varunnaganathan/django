"""error is if we try to order_by along with values using the field created using annotation"""
from django.core.exceptions import FieldError
from django.test import TestCase
from django.db.models import CharField, Case, Value, When,Count,IntegerField
from .models import Client,Table
import pdb
from django.db import connection
from pprint import pprint
class NewtestTests(TestCase):
    def setUp(self):
        Client.objects.create(name="Varun",registered_on="2015-02-25",account_type='R')
        Client.objects.create(name="Rahul",registered_on="2015-03-25",account_type='P')
        Client.objects.create(name="Radhika",registered_on="2015-04-25",account_type='G')
        Client.objects.create(name="Rakhee",registered_on="2015-05-25",account_type='G')
        Table.objects.create(value=11)
        Table.objects.create(value=10)
        #pdb.set_trace()
    
    def test_annotation_with_values_and_when(self):
        try:
            a=Client.objects.annotate(
                    discount=Case(
                        When(account_type=Client.GOLD,then=Value('5%')),
                        When(account_type=Client.PLATINUM,then=Value('10%')),
                        default=Value('0%'),
                        output_field=CharField(),
                        ),
                    ).order_by('id').values('id') 
            #print a[0]
        except AttributeError:
            print "Annotations and values with where and no where not working"
        else:
            print "NO error with annotations,case and when"
    def test_annotation_with_annotated_field(self):
        try:
        	#pdb.set_trace()
        	query=Table.objects.annotate(other=Case(
            	When(value=11,then=Value(1)),
            	When(value=10,then=Value(2)),
            	output_field=IntegerField()
            	),
            	).order_by('other').values('id')
        except AttributeError:
        	print "annotation with annotated field in orderby not working"
        else:
        	print "Annotation with annotated field in orderby working"
    """checking if it works with default annotate set value"""
    def test_annottaion_without_annotated_field(self):
        try:
        	query=Table.objects.annotate(other=Count('value')).order_by('other').values('id')
        	#print query
        except AttributeError:
        	print "annotation without annotated field not working"
        else:
        	print "annotation without annotated field working"




