from rest_framework.generics import UpdateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurant, Employee
from .serializers import RestaurantListSerializer, EmployeeListSerializer, CreateRestaurantSerializer, \
    CreateEmployeeSerializer, UpdateRestaurantSerializer


class RestaurantListView(APIView):
    def get(self, request):
        restaurant = Restaurant.objects.all()
        serializer = RestaurantListSerializer(restaurant, many=True)
        return Response(serializer.data)


class CreateRestaurantView(APIView):
    def post(self, request):
        restaurant = CreateRestaurantSerializer(data=request.data)
        if restaurant.is_valid():
            restaurant.save()
        return Response(status=201)


class UpdateRestaurantView(UpdateAPIView):
    serializer_class = UpdateRestaurantSerializer
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance = Restaurant.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})

        serializer = UpdateRestaurantSerializer(data=request.data, instance=instance)
        return Response({'post': serializer.data})


class EmployeeListView(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeListSerializer(employee, many=True)
        return Response(serializer.data)


class CreateEmployeeView(APIView):

    def post(self, request):
        restaurant = CreateEmployeeSerializer(data=request.data)
        if restaurant.is_valid():
            restaurant.save()
        return Response(status=201)
