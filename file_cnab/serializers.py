from rest_framework import serializers

from .models import FileCnab


class FileCnabSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileCnab
        fields = [
            "id", 
            "type_number", 
            "date", 
            "value", 
            "cpf", 
            "card", 
            "time", 
            "owner", 
            "store"
        ]
        read_only_fields = [
            "id", 
        ]

    def create(self, validated_data):
        instance, _ = FileCnab.objects.get_or_create(**validated_data)
        return instance
