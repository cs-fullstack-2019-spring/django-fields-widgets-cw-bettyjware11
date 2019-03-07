from django import forms
from .models import SuperHero

SUPERPOWER_CHOICES= (
    ('flight','Flight'),
    ('speed', 'Speed'),
    ('invisability','Invisability'),
    ('telekenetic','Telekenetic'),
    ('healing','Healing'),
    ('other','Other')
)

superHeroRating = (
    (0, 'Good'),
    (1, 'Kinda good'),
    (2, 'Just okay'),
    (3, 'Neutral'),
    (4, 'A Little Evil'),
    (5, 'Evil'),
)


class SuperHeroForm(forms.ModelForm):
    class Meta:
        model = SuperHero
        fields = "__all__"
        widgets = {
            "dropDown": forms.Select(choices=[("rich","Rich"), ("super powers", "Super Powers" )]),
            "dropDown2": forms.SelectMultiple(choices=SUPERPOWER_CHOICES),
            "radio": forms.RadioSelect(choices=superHeroRating),
            "checkbox": forms.CheckboxSelectMultiple(choices=SUPERPOWER_CHOICES),
        }
