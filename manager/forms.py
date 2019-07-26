from django import forms
from manager.models import receivedOrder

class courierForm(forms.ModelForm):
    orderid = models.CharField(required=False)
    otp = models.IntegerField(required=False)
    status = models.IntegerField(required=False)

    class Meta:
        model = receivedOrder
        fields = ('orderid', 'otp', 'status')
