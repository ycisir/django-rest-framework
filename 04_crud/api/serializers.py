from rest_framework import serializers
from api.models import Student

# 1: ====================== validators =============================
def start_with_y(value):
    if value[0].lower() != 'y':
        raise serializers.ValidationError('Name should start with Y')

class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, validators=[start_with_y])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        # print(instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    #2: ====================== field level validation =======================
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat full!')
        
        return value
    
    #3: ====================== object level validation =======================
    def validate(self, data):
        name = data.get('name')
        roll = data.get('roll')
        city = data.get('city')

        if name == 'Jack Sparrow' or roll == 1 or city == 'India Oceana':
            raise serializers.ValidationError('This is jack!')
        
        return data
    