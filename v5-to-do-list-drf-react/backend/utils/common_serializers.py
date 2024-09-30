from rest_framework import serializers
import humps


class PaginationParamsSerializer(serializers.Serializer):
    offset = serializers.IntegerField(required=False, default=0)
    limit = serializers.IntegerField(required=False, default=20)
    sort = serializers.CharField(required=False, default="")

    def validate_sort(self, value:str):
        if not value:
            return value
        
        value = humps.decamelize(value)
        sorting_fields = self.context.get("sorting_fields", [])
        if value.lstrip("-") not in sorting_fields:
            raise serializers.ValidationError(f"Invalid sort field: '{value}'. Valid fields are: {', '.join([humps.camelize(field) for field in sorting_fields])}")
        
        return value
    