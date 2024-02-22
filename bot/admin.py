from django.contrib import admin
from .models import UserProfile, Start, MinimalDepozitQancha, OneDeposite, CallBack, Pul, Sharhlar, SharhlarImage, Litsenziya
from django import forms


class StartAdminForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}))

    class Meta:
        model = Start
        fields = '__all__'

@admin.register(Start)
class StartAdmin(admin.ModelAdmin):
    form = StartAdminForm


class SharhlarImageInline(admin.TabularInline):
    model = SharhlarImage


class SharhlarAdmin(admin.ModelAdmin):
    inlines = [SharhlarImageInline]


admin.site.register(UserProfile)
admin.site.register(MinimalDepozitQancha)
admin.site.register(OneDeposite)
admin.site.register(CallBack)
admin.site.register(Pul)
admin.site.register(Sharhlar, SharhlarAdmin)
admin.site.register(Litsenziya)
