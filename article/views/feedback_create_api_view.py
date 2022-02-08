from unicodedata import category
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from article.serializers import FeedbackSerializer
from article.models import Feedback
from article.models import Article
from config.views import BaseView
from django.db.models import Field
from django.shortcuts import get_object_or_404

class FeedbackCreateAPIView(BaseView,
                                generics.CreateAPIView,):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def __init__(self):
        self.CATEGORY_CHOICES = (
            ('thumbs_up','thumbs_up'),
            ('heart','heart'),
            ('clap','clap'),
            ('lion','lion'),
            ('thinking','thinking'),
            ('smile','smile'),
            ('clover','clover'),
            ('eyes','eyes'),
            ('perfect','perfect'),
            ('bulb','bulb')
        )
        
    def create(self,request,category,article_id, *args, **kwargs):
        article = get_object_or_404(Article, id = article_id)
        try:
            Feedback.objects.get(user=self.current_user, article=article)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            check_category = self.check_category(category)
            if check_category:
                feedback = Feedback.objects.create(user=self.current_user, article=article,category=category)
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def check_category(self,category):
        """"check is category in category_choices"""
    
        for i in range(len(self.CATEGORY_CHOICES)):
                if category in self.CATEGORY_CHOICES[i]:
                    return True
        return False
