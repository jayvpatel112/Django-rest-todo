from rest_framework import serializers
from .models import Todo, TimingTodo
import re
from django.template.defaultfilters import slugify

class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    
    class Meta:
        model = Todo
        fields = ['user','todo_title', 'slug', 'todo_description', 'uid']
        # fields = '__all__' 
        # fields = ['todo_title']
        # exclude = ['created_at']

    def get_slug(self, obj):
        return slugify(obj.todo_title)

    def validate(self, validated_data):
        print(validated_data)
        if validated_data.get('todo_title'):
            todo_title = validated_data['todo_title']

            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if not regex.search(todo_title) == None:
                raise serializers.ValidationError('todo title can not contain special characters')
        
        return validated_data

class TimingTodoSerializer(serializers.ModelSerializer):
    todo = TodoSerializer()

    class Meta:
        model = TimingTodo
        exclude = ['created_at', 'updated_at']
        # depth = 1
        
