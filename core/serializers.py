from rest_framework.serializers import ModelSerializer
from core.models import Categoria, Editora

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = ["nome", "site"] # Quais fields serão incluídos na API