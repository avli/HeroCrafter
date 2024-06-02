from django.http import HttpRequest, JsonResponse
from rest_framework import viewsets, permissions, serializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from . import models
from .serializers import CharacterSerializer
from .util import generate_biography, generate_portrait


class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.Character.objects.filter(user=self.request.user)


class CharacterBaseView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    class Serializer(serializers.Serializer):
        name = serializers.CharField()
        alignment = serializers.CharField()
        gender = serializers.CharField()
        race = serializers.CharField()
        character_class = serializers.CharField()

    def post(self, request: HttpRequest):
        serializer = self.Serializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            alignment = serializer.validated_data.get('alignment')
            gender = serializer.validated_data.get('gender')
            race = serializer.validated_data.get('race')
            character_class = serializer.validated_data.get('character_class')
            result = self.send_request_to_ai_assistant(name, alignment, gender, race, character_class)
            return JsonResponse({"response": result})
        else:
            return JsonResponse(serializer.errors, status=400)

    def send_request_to_ai_assistant(self, *args):
        raise NotImplementedError()


class CharacterBiographyView(CharacterBaseView):
    def send_request_to_ai_assistant(self, name, alignment, gender, race, character):
        return generate_biography(name, alignment, gender, race, character)


class CharacterPortraitView(CharacterBaseView):
    def send_request_to_ai_assistant(self, name, alignment, gender, race, character):
        return generate_portrait(name, alignment, gender, race, character)
