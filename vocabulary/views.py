from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Vocabulary
from .serializers import VocabularySerializer


class VocabularyViewSet(viewsets.ModelViewSet):
    queryset = Vocabulary.objects.all().order_by("word")
    serializer_class = VocabularySerializer

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ["word", "pinyin", "meaning_ar"]
    ordering_fields = ["word", "hsk_level"]

     # Filter vocabulary by HSK level
    def get_queryset(self):
        queryset = Vocabulary.objects.all()

        hsk_level = self.request.query_params.get("hsk_level")

        if hsk_level:
            queryset = queryset.filter(hsk_level=hsk_level)

        return queryset.order_by("word")