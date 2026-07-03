from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import IdeaAnalysisRequestSerializer
from .services.analyzer import analyze_idea


class IdeaAnalysisView(APIView):

    def post(self, request):

        serializer = IdeaAnalysisRequestSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        result = analyze_idea(
            serializer.validated_data["idea_text"]
        )

        return Response(
            result,
            status=status.HTTP_200_OK
        )