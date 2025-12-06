from django.shortcuts import render
from .models import Deals
from .forms import DealForm
def look_home(request):
    deals = Deals.objects.all()
    return render(request, 'main/look.html', {'deals': deals})


def edit(request):
    deals = Deals.objects.all()
    selected_deal = None
    form = None

    if request.method == 'POST':
        deal_id = request.POST.get('deal_id')  # получаем id выбранного дела из формы выбора
        if deal_id:
            selected_deal = Deals.objects.get(pk=deal_id)
            form = DealForm(request.POST, instance=selected_deal)
            if form.is_valid():
                form.save()
                return render(request, 'main/index.html')
    else:
        deal_id = request.GET.get('deal_id')
        if deal_id:
            selected_deal = Deals.objects.get(pk=deal_id)
            form = DealForm(instance=selected_deal)

    context = {
        'deals': deals,
        'selected_deal': selected_deal,
        'form': form,
    }
    return render(request, 'main/edit.html', context)