from django.db.models import QuerySet

class UserOwnedQuerysetMixin:
    """
    A mixin to add filter 'created by' field to get only objects owned by the current user 
    
    Uses: Add this mixin to view class
    """
    def get_queryset(self):
        queryset = super().get_queryset()
        if isinstance(queryset, QuerySet):
            return queryset.filter(created_by=self.request.user)
        return queryset