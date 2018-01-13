from . import views

from django.conf.urls import url

urlpatterns = [
    url(r'^communities/cfp/add/$', views.CommunityCreate.as_view(), name='community-add'),
    url(r'^communities/cfp/(?P<slug>[^/]+)/participate/$', views.ParticipationUpdate.as_view(), name='community-participate'),
    url(r'^communities/cfp/(?P<slug>[^/]+)/dont-participate/$', views.NotParticipating.as_view(), name='community-not-participating'),
    url(r'^communities/cfp/(?P<slug>[^/]+)/edit/$', views.CommunityUpdate.as_view(), name='community-update'),
    url(r'^communities/cfp/(?P<community_slug>[^/]+)/add/$', views.ProjectUpdate.as_view(), name='project-participate'),
    url(r'^communities/cfp/(?P<community_slug>[^/]+)/status/$', views.community_status_change, name='community-status'),
    url(r'^communities/cfp/(?P<community_slug>[^/]+)/coordinator-update/(?P<coordinator_id>[^/]+)/$', views.community_coordinator_update, name='community-coordinator-update'),
    url(r'^communities/cfp/(?P<community_slug>[^/]+)/(?P<project_slug>[^/]+)/mentor-status/(?P<mentor_id>[^/]+)/$', views.project_mentor_update, name='project-mentor-status'),
    url(r'^communities/cfp/(?P<community_slug>[^/]+)/(?P<project_slug>[^/]+)/mentor-create/$', views.MentorApprovalUpdate.as_view(), name='project-mentor-create'),
    url(r'^communities/cfp/(?P<community_slug>[^/]+)/(?P<project_slug>[^/]+)/edit/$', views.ProjectUpdate.as_view(), name='project-participate'),
    url(r'^communities/cfp/(?P<community_slug>[^/]+)/(?P<project_slug>[^/]+)/status/$', views.project_status_change, name='project-status'),
    url(r'^communities/cfp/(?P<community_slug>[^/]+)/(?P<project_slug>[^/]+)/$', views.project_read_only_view, name='project-read-only'),
    url(r'^communities/cfp/(?P<slug>[^/]+)/$', views.community_read_only_view, name='community-read-only'),
    url(r'^(?P<round_slug>[^/]+)/communities/(?P<slug>[^/]+)/$', views.community_landing_view, name='community-landing'),
    url(r'^communities/cfp/$', views.community_cfp_view, name='community-cfp'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^account/$', views.ComradeUpdate.as_view(), name='account'),
    url(r'^register/$', views.RegisterUser.as_view(), name='register'),
    url(r'^register/sent/$', views.PendingRegisterUser.as_view(), name='registration_complete'),
    url(r'^register/activate/(?P<activation_key>[-.:\w]+)/$', views.ActivationView.as_view(), name='registration_activate'),
    url(r'^register/activate/$', views.ActivationCompleteView.as_view(), name='registration_activation_complete'),
]
