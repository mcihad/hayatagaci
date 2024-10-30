from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from yardim.models import Ogrenci
from .serializers import OgrenciSerializer


class OgrenciRetrieveViewByKartNo(generics.RetrieveAPIView):
    queryset = Ogrenci.objects.all()
    serializer_class = OgrenciSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.data["bakiye"] = self.get_object().bakiye or 0
        return response

    def get_object(self):
        kart_no = self.kwargs.get("kart_no")
        try:
            return Ogrenci.objects.get(kart_no=kart_no, okul=self.request.user.okul)
        except Ogrenci.DoesNotExist:
            raise Http404
