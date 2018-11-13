from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .models import Adnabu
from .serializers import AdnabuSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class adnabuapi(APIView):
    serializer_class = AdnabuSerializer

    def post(self,request,*args,**kwargs):
    	data = request.data
    	email = data['email']
    	url = data['url']
    	urls = url.split(",")
    	serializer = AdnabuSerializer(data=data)
    	if serializer.is_valid():
    		template = get_template('adnabuapi.txt')
    		context = {
    		'email': email,
    		'urls': urls,
    		}
    		content = template.render(context)
    		email = EmailMessage(
    			"New adnabu form submission",
    			content,
    			"adnabu.com" +'',
    			[email],
    			headers = {'Reply-To': email }
    			)
    		email.send()
    		serializer.save()
    		resp = serializer.data
    		resp['urls'] = url.split(",")
    		return Response({'detail':resp})

    	return Response({'detail':"Something Went Wrong Please tryagain !!!"})    
