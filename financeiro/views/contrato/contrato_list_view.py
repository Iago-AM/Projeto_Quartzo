from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from ...models import Contrato


class ContratoListView(LoginRequiredMixin, ListView):
    model = Contrato
    template_name = 'contrato_list_view.html'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

    

        return context
