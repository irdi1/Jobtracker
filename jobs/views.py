from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job
from .serializers import JobSerializer

# Create your views here.
class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status']
    search_fields = ['position', 'company']
    permission_classes = [permissions.IsAuthenticated]
    # queryset = Job.objects.all()

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)