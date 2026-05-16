import random
from django.shortcuts import render, redirect
from .models import LottoRound, LottoTicket

def lotto_index(request):
    curr_round = LottoRound.objects.last()
    tickets = None
    
    if request.user.is_authenticated:
        tickets = LottoTicket.objects.filter(user=request.user).order_by('-purchase_date')
    
    return render(request, 'lotto/index.html', {
        'current_round': curr_round,
        'user_tickets': tickets
    })

def purchase_lotto(request):
    if request.method == 'POST':
        r = LottoRound.objects.last()
        
        if 'buy_auto' in request.POST:
            nums = sorted(random.sample(range(1, 46), 6))
            sel_type = 'AUTO'
        else:
            nums = [
                int(request.POST.get('num1', 1)),
                int(request.POST.get('num2', 1)),
                int(request.POST.get('num3', 1)),
                int(request.POST.get('num4', 1)),
                int(request.POST.get('num5', 1)),
                int(request.POST.get('num6', 1)),
            ]
            nums.sort()
            sel_type = 'MANUAL'

        LottoTicket.objects.create(
            user=request.user,
            lotto_round=r,
            n1=nums[0], n2=nums[1], n3=nums[2],
            n4=nums[3], n5=nums[4], n6=nums[5],
            selection_type=sel_type
        )
        return redirect('lotto_index')