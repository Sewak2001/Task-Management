from rest_framework import serializers
from accounts.models import CustomUser
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
  members = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all())

  class Meta:
      model = Task
      fields = '__all__'

  def validate_members(self, value):
    """Ensure members list is valid, but allow it to be empty."""
    if value is None:
        return []
    return value

  def validate_status(self, value):
    """Ensure status is one of the predefined choices."""
    valid_statuses = ["Todo", "Inprogress", "Done"]
    if value not in valid_statuses:
        raise serializers.ValidationError("Invalid status. Must be one of: Todo, Inprogress, Done.")
    return value