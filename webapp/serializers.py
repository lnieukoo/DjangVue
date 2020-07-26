from rest_framework.authentication import TokenAuthentication
from rest_framework import serializers, mixins, viewsets
#from .models import Enquiries

# Serializers define the API representation.

#class EnquiriesSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Enquiries
        #fields = ('__all__')

# ViewSets define the view behavior.
#class EnquiriesViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    #authentication_classes = (TokenAuthentication, )
    #queryset = Enquiries.objects.all()
    #serializer_class = EnquiriesSerializer

