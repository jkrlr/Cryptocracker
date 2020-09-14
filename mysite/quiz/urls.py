from django.conf.urls import include, url
from . import views

urlpatterns = [
        url('past',views.past,name="past"),
        url('live',views.live,name="live"),
        url('future',views.future,name="future"),


        url('past/(?P<hello>[0-9]+)/',views.past_contest,name='past_contest'),
        # url(r'^past/(?P<hello>[0-9]+)/leaderboard/$',views.past_leader,name='past_leader'),
        url('(?P<hello>[0-9]+)/',views.contest,name='contest'),
        url('(?P<hello>[0-9]+)/submit',views.submit,name='submit'),
        url('(?P<hello>[0-9]+)/live/',views.live_contest,name='live_contest'),
        url('(?P<hello>[0-9]+)/register/',views.register,name='register'),
        url('(?P<hello>[0-9]+)/registeration/',views.registeration,name='registeration'),
        url('(?P<hello>[0-9]+)/live/leaderboard/',views.live_leaderboard,name='live_leaderboard'),
        url('(?P<hello>[0-9]+)/live/get_leaderboard',views.get_live_leaderboard,name='live_leaderboard'),
        url('past/(?P<hello>[0-9]+)/leaderboard/',views.leaderboard,name='leaderboard'),

        url('create_contest',views.create_contest,name="create_contest"),
        url('edit_contest/(?P<contest_id>[0-9]+)',views.edit_contest, name='edit_contest'),

        url('(?P<contest_id>[0-9]+)/ajax',views.ajax_q,name="ajax_q"),
]
