from rest_framework import serializers

from .models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        exclude = ['user']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ability_scores'] = {}

        for ability_score_name in ("strength", "dexterity", "constitution",
                                   "intelligence", "wisdom", "charisma", "hit_points"):
            representation['ability_scores'][ability_score_name] = representation.pop(ability_score_name)

        return representation
