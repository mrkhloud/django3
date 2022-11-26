from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """
    Построение пути к файлу. Формат (media)/avatar/user_id/photo.jpg
    """

    return f'avatar/{instance.id}/{file}'


def validate_size_image(file):
    """
    Проверка размера изображения
    """
    megabyte_limit = 2
    if file.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f'Размер файла больше чем {megabyte_limit}MB!')
