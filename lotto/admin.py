import random
from django.contrib import admin
from django.utils import timezone
from .models import LottoRound, LottoTicket

@admin.action(description='선택 회차 즉시 추첨')
def do_draw(modeladmin, request, queryset):
    for r in queryset:
        if r.is_drawn:
            continue
            
        nums = sorted(random.sample(range(1, 46), 7))
        r.num1, r.num2, r.num3, r.num4, r.num5, r.num6 = nums[:6]
        r.bonus_num = nums[6]
        r.is_drawn = True
        r.draw_date = timezone.now()
        r.save()
        
        win_set = set(nums[:6])
        bonus = nums[6]
        tickets = LottoTicket.objects.filter(lotto_round=r)
        
        for t in tickets:
            t_set = {t.n1, t.n2, t.n3, t.n4, t.n5, t.n6}
            match_cnt = len(win_set.intersection(t_set))
            
            if match_cnt == 6: t.rank = 1
            elif match_cnt == 5 and (bonus in t_set): t.rank = 2
            elif match_cnt == 5: t.rank = 3
            elif match_cnt == 4: t.rank = 4
            elif match_cnt == 3: t.rank = 5
            else: t.rank = 0
            t.save()

class LottoRoundAdmin(admin.ModelAdmin):
    list_display = ['round_number', 'is_drawn', 'winning_numbers']
    actions = [do_draw]

    def winning_numbers(self, obj):
        if obj.is_drawn:
            return f"{obj.num1}, {obj.num2}, {obj.num3}, {obj.num4}, {obj.num5}, {obj.num6} + [{obj.bonus_num}]"
        return "추첨 전"

class LottoTicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'lotto_round', 'selection_type', 'rank']

admin.site.register(LottoRound, LottoRoundAdmin)
admin.site.register(LottoTicket, LottoTicketAdmin)