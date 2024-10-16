
from django.db.models.base import ModelBase
import django_filters
from rest_framework import serializers
from auditlog.registry import auditlog
from typing import Dict, List, Tuple
from rest_framework import permissions, viewsets, routers
from django.urls import URLResolver, include, path

class CRUDAppRegistry:
    def __init__(self):
        self._registry: List[Tuple[URLResolver, viewsets.ModelViewSet]] = []
        
    def register(self, model: ModelBase, audit=True):
        if audit:
            auditlog.register(model)
        
        """
        self.model = model
        class Meta:
            model = self.model
            fields = ['name', 'email', 'created_at']
        self.meta = Meta
        class GeneralSerializer(serializers.HyperlinkedModelSerializer):
            Meta = self.meta
        """
        
        class GeneralSerializer(serializers.HyperlinkedModelSerializer):
            class Meta:
                pass
        GeneralSerializer.Meta.model = model
        GeneralSerializer.Meta.fields = ['name', 'email', 'created_at']
                
        class GeneralViewSet(viewsets.ModelViewSet):
            queryset = model.objects.all()
            serializer_class = GeneralSerializer
            lookup_field = ('pk')
            #permission_classes = [permissions.IsAuthenticated]
            filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
            filterset_fields = ['name', 'email']
            #def get_queryset(self):
        
        model_name = model.__name__.lower()+'s'
        print('Registering', model_name)
        router = routers.DefaultRouter()
        router.register(model_name, GeneralViewSet)
        
        self._registry.append((path('/api/', include(router.urls)), GeneralViewSet))
        
        
crudRegistry = CRUDAppRegistry()