from rest_framework import serializers

from .models import FooModel


class FooSerializer(serializers.ModelSerializer):
	class Meta:
		model = FooModel

		#the selializer specifies/restricts the fields to return for each API method (get, post, etc)
		fields = [
		'country_name','presidents_name','ethnicity'
		]
			
		