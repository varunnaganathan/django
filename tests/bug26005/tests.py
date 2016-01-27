from __future__ import unicode_literals

import datetime
from decimal import Decimal

from django.core.exceptions import FieldDoesNotExist, FieldError
from django.db.models import (
    F, BooleanField, CharField, Count, DateTimeField, ExpressionWrapper, Func,
    IntegerField, Sum, Value,
)
from django.utils.encoding import uri_to_iri
from django.test import TestCase
from django.utils import six
import pdb

class FirstTestCase(TestCase):
	def setUp(self):
		pass
	def test_first(self):
		pdb.set_trace()
                self.assertEqual(uri_to_iri(uri_to_iri("%2E%252E")),uri_to_iri("%2E%252E"))
		
