def validate_image_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpeg', '.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            'Unsupported file extension. Only ( jpeg , jpg , png )')


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpeg', '.jpg', '.png', 'pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            'Unsupported file extension. Only ( jpeg , jpg , png , pdf )')
