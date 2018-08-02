from django.conf.urls import url
from .views import *
urlpatterns = [
    #http://localhost:8000/01_add/
    url(r'^01_add/$',add_views),
    #http://localhost:8000/02_query/
    url(r'^02_query/$',query_views),
    #http://localhost:8000/03_aulist/
    url(r'^03_aulist/$',aulist_views),
    #http://localhost:8000/04_delete/ID
    url(r'^04_delete/(\d+)/$',delete_views,name='del'),
    #http://localhost:8000/05_upshow/ID
    url(r'^05_upshow/(\d+)/$',upshow_views,name='up'),
    #http://localhost:8000/06_upage
    url(r'^06_upage/$',upage_views),
    #http://localhost:8000/07_doQ/
    url(r'^07_doQ/$',doQ_views),
    #http://localhost:8000/08_raw/
    url(r'^08_raw/$',raw_views),
    #http://localhost:8000/09_oto/
    url(r'^09_oto/$',oto_views),
    #http://localhost:8000/10_otm/
    url(r'^10_otm/$',otm_views),
    #http://localhost:8000/11_mtm/
    url(r'^11_mtm/$',mtm_views),
    #http://localhost:8000/12_obj
    url(r'^12_obj/$',obj_views),
    #http://localhost:8000/13_update/
    url(r'^13_update/$',update_views,name='update'),
]