from django import forms

from score.models import Restaurant, Menu, Employee, Scores


class CreateRestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'


class CreateMenuForm(forms.ModelForm):

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['restaurant_field'] = forms.ChoiceField(
            choices=[(rt.pk, f'{rt.name}') for rt in self.instance.restaurant.all()],
            label='Restaurant',
        )
        self.fields['restaurant_field'].choices.insert(0, (0, '--------'))

    class Meta:
        model = Menu
        fields = '__all__'


class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class VoteMenuForm(forms.ModelForm):
    model_employee = Employee

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['voter_field'] = forms.ChoiceField(
            choices=[(em.pk, f'{em.first_name} {em.last_name}')
                     for em in self.model_employee.objects.all()],
            label='Employee',
        )
        self.fields['vote_field'] = forms.ChoiceField(
            choices=[(vt.pk, f'{vt.vote}') for vt in self.instance.score.all()],
            label='Vote',
        )

    class Meta:
        model = Scores
        fields = '__all__'
        exclude = ('menu',)
