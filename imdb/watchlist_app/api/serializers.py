from django.db.models import fields
from rest_framework import serializers, validators
from watchlist_app.models import Movie


################################################### ModelSerializer #####################################################
# No need to define get, post and put explicityly
# But validators must be defined explicitly
class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()  # Create Custom Serializer field

    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ["id","name","description"]
        # exclude = ["active"]

    # Method for  Custom Serializer field
    def get_len_name(self, object):
        return len(object.name)

    # Field Level Validators for "name" field
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Movie name is too short")
        else:
            return value

     # Object Level Validators
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError(
                "Movie name & description must not be same")
        else:
            return data


################################################### Serializers #########################################################
# # 1. Validators
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")
#     else:
#         return value


# #  Create the serializer for "Movie"  model
# class MovieSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   name = serializers.CharField(validators=[name_length])
#   description = serializers.CharField()
#   active = serializers.BooleanField()


#   # Serializer for POST request
#   def create(self, validated_data):
#       return Movie.objects.create(**validated_data)


#   # Serializer for PUT request
#   def update(self, instance, validated_data):
#       # instance is the updated data
#       # validated_data is the old data
#       instance.name = validated_data.get('name',instance.name)
#       instance.description = validated_data.get('description',instance.description)
#       instance.active = validated_data.get('active',instance.active)
#       instance.save()
#       return instance


#   # 2. Field Level Validators for "name" field
#   def validate_name(self, value):
#       if len(value) < 2:
#           raise serializers.ValidationError("Movie name is too short")
#       else:
#           return value


#   # 3. Object Level Validators
#   def validate(self, data):
#       if data['name'] == data['description']:
#           raise serializers.ValidationError("Movie name & description must not be same")
#       else:
#           return data
