from django.db import models
from django.contrib.auth.models import User

class LottoRound(models.Model):
    round_number = models.IntegerField(unique=True)
    draw_date = models.DateTimeField(null=True, blank=True)
    is_drawn = models.BooleanField(default=False)
    
    num1 = models.IntegerField(null=True, blank=True)
    num2 = models.IntegerField(null=True, blank=True)
    num3 = models.IntegerField(null=True, blank=True)
    num4 = models.IntegerField(null=True, blank=True)
    num5 = models.IntegerField(null=True, blank=True)
    num6 = models.IntegerField(null=True, blank=True)
    bonus_num = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.round_number}회차"

class LottoTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lotto_round = models.ForeignKey(LottoRound, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    
    n1 = models.IntegerField()
    n2 = models.IntegerField()
    n3 = models.IntegerField()
    n4 = models.IntegerField()
    n5 = models.IntegerField()
    n6 = models.IntegerField()
    
    selection_type = models.CharField(max_length=10)
    rank = models.IntegerField(default=-1)

    def __str__(self):
        return f"{self.user.username} - {self.lotto_round.round_number}회"