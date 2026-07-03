from django.urls import path
from .views import IdeaAnalysisView

urlpatterns = [
    path("analyze/", IdeaAnalysisView.as_view(), name="idea-analysis"),
]