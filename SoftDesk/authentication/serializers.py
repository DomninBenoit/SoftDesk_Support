from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'age', 'consent']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            age=validated_data['age'],
            consent=validated_data['consent']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            # mise à jour une par une des clés restantes dans 'validated_data'
            setattr(instance, key, value)

        if password:
            # si 'password' est présent, on met à jour le mot de passe
            instance.set_password(password)
        instance.save()

        return instance
