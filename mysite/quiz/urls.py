from django.urls import include, path, re_path
from . import views

urlpatterns = [
        path('past',views.past,name="past"),
        path('live',views.live,name="live"),
        path('future',views.future,name="future"),


        path('past/<int:hello>/',views.past_contest,name='past_contest'),
        # url(r'^past/(?P<hello>[0-9]+)/leaderboard/$',views.past_leader,name='past_leader'),
        path('<int:hello>/',views.contest,name='contest'),
        path('<int:hello>/submit',views.submit,name='submit'),
        path('<int:hello>/live/',views.live_contest,name='live_contest'),
        path('<int:hello>)/register/',views.register,name='register'),
        path('<int:hello>/registeration/',views.registeration,name='registeration'),
        path('<int:hello>/live/leaderboard/',views.live_leaderboard,name='live_leaderboard'),
        path('<int:hello>/live/get_leaderboard',views.get_live_leaderboard,name='live_leaderboard'),
        path('past/<int:hello>/leaderboard/',views.leaderboard,name='leaderboard'),

        path('create_contest',views.create_contest,name="create_contest"),
        path('edit_contest/<int:contest_id>',views.edit_contest, name='edit_contest'),

        path('<int:contest_id>/ajax',views.ajax_q,name="ajax_q"),
]
