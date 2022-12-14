from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from Emp_Login_app.serializers import UserRegister

class LoginView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  
        }
        return Response(content)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username':user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'user_id': user.pk,
            'email': user.email,
            'admin':user.is_superuser,
        })

class register(APIView):
      def post(self,request,format=None):

        serializer=UserRegister(data=request.data)

        data={}

        if serializer.is_valid():

            account=serializer.save()

            data['response']='registered'

            data['username']=account.username

            data['email']=account.email

            token,create=Token.objects.get_or_create(user=account)

            data['token']=token.key

        else:

            data=serializer.errors

        return Response(data)



class register(APIView):
    def post(self,request,format=None):

        serializer=UserRegister(data=request.data)

        data={}

        if serializer.is_valid():

            account=serializer.save()

            data['response']='registered'

            data['username']=account.username

            data['email']=account.email

            token,create=Token.objects.get_or_create(user=account)

            data['token']=token.key

        else:

            data=serializer.errors

        return Response(data)