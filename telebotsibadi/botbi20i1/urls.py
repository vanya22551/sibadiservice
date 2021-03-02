from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, facePage, group, labsPage, studentPage, FileChangeView, FileDeleteView
from .views import update_changes,lab_add_view, LoginUserView, RegisterUserView, LogoutView, user, ChangePasswordView, \
    FileAddView, view_info
urlpatterns = [
    path('', facePage, name='face_page'),
    path(r'face_page', facePage, name='face_page'),
    path(r'json_response/<int:index_id>/', index, name='index_page'),
    path(r'group/<int:group_id>/', group, name='group_page'),
    path(r'lab/<int:id>/', labsPage, name='labs_page'),
    path(r'student/<int:id>/', studentPage, name='student_page'),
    path(r'api/v1/update_stats_status', update_changes, name='update_api'),
    path(r'addlab', lab_add_view, name='addlab_page'),
    path(r'login', LoginUserView.as_view(), name='login_page'),
    path(r'user', user, name='user_page'),
    path(r'registration', RegisterUserView.as_view(), name='register_page'),
    path(r'changepassword', ChangePasswordView, name='changepassword_page'),
    path(r'addfile', FileAddView, name='add_file'),
    path(r'changefile', FileChangeView, name='change_file'),
    path(r'delete_file', FileDeleteView, name='delete_file'),
    path(r'info', view_info, name='info'),
    path(r'logout', LogoutView.as_view(next_page = 'face_page'), name='logout')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)