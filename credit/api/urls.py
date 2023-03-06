from django.urls import path
from .views import ListCardsView, DetailCardView, NewCardView, UpdateCardView, DeleteCardView

app_name = 'api'

urlpatterns = [
    path('cards/', ListCardsView.as_view(), name='list_cards'),
    path('cards/<int:pk>/', DetailCardView.as_view(), name='detail_card'),
    path('cards/new/', NewCardView.as_view(), name='new_card'),
    path('cards/<int:pk>/edit/', UpdateCardView.as_view(), name='update_card'),
    path('cards/<int:pk>/delete/', DeleteCardView.as_view(), name='delete_card'),
]