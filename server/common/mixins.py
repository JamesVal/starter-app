from rest_framework import serializers

class RequiredFieldsMixin:
    required_fields = {}

    def validate_required_fields(self, data):
        errors = {}
        for field_name, error_message in self.required_fields.items():
            if not data.get(field_name):
                errors[field_name] = error_message
        if errors:
            raise serializers.ValidationError(errors)
        return data

    def validate(self, data):
        data = super().validate(data)
        data = self.validate_required_fields(data)
        return data

class SaveOwnerAccountMixin:

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].selected_account
        return super().create(validated_data)

class CombinedMixin(RequiredFieldsMixin, SaveOwnerAccountMixin):
    pass
