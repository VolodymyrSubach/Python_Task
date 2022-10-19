from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from score.forms import CreateRestaurantForm, CreateMenuForm, CreateEmployeeForm, VoteMenuForm
from score.models import Restaurant, Employee, Menu, Scores


class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant/list.html'


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/list.html'


class MenuListView(ListView):
    model = Menu
    template_name = 'menu/list.html'


class CreateRestaurantView(CreateView):
    model = Restaurant
    form_class = CreateRestaurantForm
    success_url = reverse_lazy('restaurant:list')
    template_name = 'restaurant/create.html'


class CreateMenuView(CreateView):
    model = Menu
    form_class = CreateMenuForm
    template_name = 'menu/create.html'
    success_url = reverse_lazy('menu:list')

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['restaurant_field'] = self.object.restaurant.pk
        except AttributeError:
            initial['restaurant_field'] = 0

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        pk = int(form.cleaned_data['restaurant_field'])
        if pk:
            form.instance.restaurant = Restaurant.objects.get(pk=pk)
        else:
            form.instance.restaurant = None
        form.save()

        return response


class VoteMenuView(CreateView):
    model = Scores
    form_class = VoteMenuForm
    success_url = reverse_lazy('menu:list')
    template_name = 'menu/vote.html'

    # def get_initial(self):
    #     initial = super().get_initial()
    #     try:
    #         initial['vote_field'] = self.object.score.pk
    #     except AttributeError:
    #         initial['vote_field'] = 0
    #
    #     return initial
    #
    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     pk = int(form.cleaned_data['vote_field'])
    #     if pk:
    #         form.instance.score = Menu.objects.get(pk=pk)
    #     else:
    #         form.instance.score = None
    #     form.save()
    #
    #     return response


class CreateEmployeeView(CreateView):
    model = Employee
    form_class = CreateEmployeeForm
    template_name = 'employee/create.html'
    success_url = reverse_lazy('employee:list')
