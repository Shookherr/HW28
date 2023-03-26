from django.conf.urls.static import static
from django.urls import path

from HW28 import settings
from ads.views.ad import AdListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView, AdUploadImage

urlpatterns = [


    path('', AdListView.as_view(), name='all_category'),
    path('<int:pk>', AdDetailView.as_view(), name='category_detail'),
    path('create/', AdCreateView.as_view(), name='category_create'),
    path('<int:pk>/update/', AdUpdateView.as_view()),
    path('<int:pk>/delete/', AdDeleteView.as_view()),

    path('<int:pk>/upload_image/',  AdUploadImage.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
