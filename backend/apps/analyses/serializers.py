from rest_framework import serializers


class IdeaAnalysisRequestSerializer(serializers.Serializer):
    idea_text = serializers.CharField(min_length=10)