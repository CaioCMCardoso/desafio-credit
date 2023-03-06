from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from api.models import Card
from django.http import JsonResponse

class ListCardsView(ListView):
    model = Card
    queryset = Card.objects.all()
    context_object_name = 'cards'

    def get(self, request, *args, **kwargs):
        cards = list(self.get_queryset().values())
        return JsonResponse(cards, safe=False)

class DetailCardView(DetailView):
    model = Card
    queryset = Card.objects.all()
    context_object_name = 'card'

    def get(self, request, *args, **kwargs):
        card = self.get_object()
        return JsonResponse(card.to_dict(), safe=False)

class NewCardView(CreateView):
    model = Card
    fields = ['exp_date', 'holder', 'number', 'cvv']
    success_url = reverse_lazy('list_cards')

class UpdateCardView(UpdateView):
    model = Card
    fields = ['exp_date', 'holder', 'number', 'cvv']
    success_url = reverse_lazy('list_cards')

class DeleteCardView(DeleteView):
    model = Card
    success_url = reverse_lazy('list_cards')