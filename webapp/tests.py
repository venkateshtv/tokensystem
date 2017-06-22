from django.test import TestCase

# Create your tests here.
from django.db import models
from webapp.models import Vendor, Token, Barcode
import datetime
import barcodevalidator
import BarcodeView
import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class validateTest1 (TestCase):

	def validateTokenCountNoDate(self):
		BarcodeView.addBarcodeNumber(1111,'B1')
		BarcodeView.addBarcodeNumber(1112,'B2')

		barcodevalidator.insertToken(1111,1)
		barcodevalidator.insertToken(1112,1)
		barcodevalidator.insertToken(1111,2)

		print "barcode added!"

		self.assertEqual(barcodevalidator.countToken(None,None,None,1), 2)

		logger.info("No Dates, barcode: 1111, vendor v1 " + str(barcodevalidator.countToken(None,None,1111,1))) 
		self.assertEqual(barcodevalidator.countToken(None,None,1111,1), 1)

		self.assertEqual(barcodevalidator.countToken(None,None,1112,1), 1)

class validateTest2 (TestCase):

	def tests(self):

		BarcodeView.addBarcodeNumber(1111,'B1')
		BarcodeView.addBarcodeNumber(1112,'B2')

		date = datetime.now()
		yesterday = datetime.now() + timedelta(days = -1)
		tomorrow = datetime.now() + timedelta(days = 1)
		
		insertDateTime = Token(tokenDateTime = yesterday, vendor = Vendor.objects.get(vendorName = 'V1'), barcode= Barcode.objects.get(barcode = 1111))
		insertDateTime.save()

		insertDateTime = Token(tokenDateTime = date, vendor = Vendor.objects.get(vendorName = 'V1'), barcode = Barcode.objects.get(barcode = 1111))
		insertDateTime.save()

		insertDateTime = Token(tokenDateTime = tomorrow, vendor = Vendor.objects.get(vendorName = 'V1'), barcode = Barcode.objects.get(barcode = 1111))
		insertDateTime.save()

		insertDateTime = Token(tokenDateTime = date, vendor = Vendor.objects.get(vendorName = 'V1'), barcode = Barcode.objects.get(barcode = 1112))
		insertDateTime.save()

		insertDateTime = Token(tokenDateTime = tomorrow, vendor = Vendor.objects.get(vendorName = 'V2'), barcode = Barcode.objects.get(barcode = 1112))
		insertDateTime.save()


		self.assertEqual(barcodevalidator.countToken(None,None,None,1), 2)

		self.assertEqual(barcodevalidator.countToken(None,date.strftime("%m/%d/%Y %H:%M:%S"),None,1), 2)

		self.assertEqual(barcodevalidator.countToken(yesterday.strftime("%m/%d/%Y %H:%M:%S"),date.strftime("%m/%d/%Y %H:%M:%S"),1111,1), 2)

		self.assertEqual(barcodevalidator.countToken(date.strftime("%m/%d/%Y %H:%M:%S"),tomorrow.strftime("%m/%d/%Y %H:%M:%S"),1112,1), 1)



		




		

