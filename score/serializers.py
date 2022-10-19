from rest_framework import serializers

from .models import Restaurant, Employee


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name')


class CreateRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class UpdateRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            'name',
            'kichen_type'
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.kichen_type = validated_data.get('kichen_type', instance.kichen_type)
        instance.save()
        return instance


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        field = ('first_name', 'last_name')


class CreateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
