from django.contrib import messages
from django.contrib.auth.decorator import login_required
from django.shortcuts import redirect, render

from .forms import ImageCreateForm


@login_required
def image_create(request):
    template_name = 'images/image/create.html'

    if request.method == 'POST':
        # form is sent
        from = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # from data is valid
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # assign current user to the item
            new_image.user = request.user
            new_image.save()
            message.success(request, 'Image added successfully')
            # redirect to new created item detail view
            return redirect(new_image.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)

    context = {
        'form': form,
        'section': 'image',
    }

    return render(request, template_name, context=context)
