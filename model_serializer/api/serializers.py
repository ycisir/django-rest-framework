from rest_framework import serializers
from api.models import Student


# 1: ====================== validators =============================
def start_with_y(value):
    if value[0].lower() != 'y':
        raise serializers.ValidationError('Name should start with Y')
    
class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields = ['name', 'roll']
        # extra_kwargs = {'name':{'read_only':True}}

    #2: ====================== field level validation =======================
    def validate_roll(self, value):
        if value > 11:
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



