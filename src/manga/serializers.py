from rest_framework import serializers

from .models import Manga, Images, Comments, Genre


class MangaListSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()

    class Meta:
        model = Manga
        fields = ['id', 'title', 'year', 'poster']

    def get_poster(self, obj):
        request = self.context.get('request')

        if obj.poster:
            return request.build_absolute_uri(obj.poster.url)
        return None


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id', 'img']


class CommentsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    nickname = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = ['username', 'nickname', 'avatar', 'comment']

    def get_username(self, obj):
        return obj.user.username

    def get_nickname(self, obj):
        return obj.user.nickname

    def get_avatar(self, obj):
        request = self.context.get('request')
        if obj.user.avatar:
            return request.build_absolute_uri(obj.user.avatar.url)
        return None


class MangaDetailSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name', read_only=True)
    genre = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    poster = serializers.SerializerMethodField()
    images = ImagesSerializer(many=True)
    comments = CommentsSerializer(many=True)

    class Meta:
        model = Manga
        fields = ['id', 'title', 'year', 'poster', 'type', 'genre', 'synopsis', 'images', 'comments']

    def get_poster(self, obj):
        request = self.context.get('request')

        if obj.poster:
            return request.build_absolute_uri(obj.poster.url)
        return None


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        exclude = ('user',)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'