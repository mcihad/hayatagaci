from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ThTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        if hasattr(user, "okul"):
            token["oid"] = user.okul.id
        token["username"] = user.username
        return token
