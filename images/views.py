from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .forms import ImageUploadForm
from .models import UploadImage
from PIL import Image


def image_upload(request):
    """ сохраняет загруженное пользователем изображение """
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save()
            new_item.coordinates = new_item.exif['GPSPosition']['num']
            new_item = form.save()
            messages.success(request, "Изображение успешно добавлено на сайт")
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageUploadForm()

    context = {'form': form}
    return render(request, 'images/upload_image.html', context=context)


def image_detail(request, id):
    """ просмотр данных об изображении """
    image = get_object_or_404(UploadImage, id=id)
    context = {'image': image}
    return render(request, 'images/image_detail.html', context)


class ImageListView(generic.ListView):
    """ выводит все изображения на страницу """
    model = UploadImage
    template_name = 'images/images_list.html'
    paginate_by = 10
