from api.serializers import CardSerializer
from rest_framework import viewsets, permissions
from api.models import Card

# Create your views here.
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]