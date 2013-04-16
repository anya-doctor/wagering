from wagers.views import WagerView, WagerPayoutView, WagerDeleteView, WagerCreateView
from wagers.views import ResetEverythingView, WagerOpenView, WagerCloseView, WagerListView
from wagers.views import WagerHistoryView, AddTournament, TournamentDetails, JoinTournament
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import permission_required, login_required

urlpatterns = patterns('',
    url(r'^tournaments/([a-f0-9]{32})$', login_required(TournamentDetails.as_view()), name="tournament-details"),
    url(r'^tournaments/join/', JoinTournament.as_view(), name="join-tournament"),
    url(r'^tournaments/add/$', login_required(AddTournament.as_view()), name="add-tournament"),
    url(r'^wagers/tourneyreset', permission_required("wagers.delete_wager")(ResetEverythingView.as_view())),
    url(r'^wagers/index/', login_required(WagerListView.as_view())),
    url(r'^wagers/history/', login_required(WagerHistoryView.as_view())),
    url(r'^wagers/delete/', permission_required("wagers.delete_wager")(WagerDeleteView.as_view())),
    url(r'^wagers/add/', permission_required("wagers.add_wager")(WagerCreateView.as_view())),
    url(r'^wagers/open/', permission_required("wagers.change_wager")(WagerOpenView.as_view())),
    url(r'^wagers/close/', permission_required("wagers.change_wager")(WagerCloseView.as_view())),
    url(r'^wagers/payout/', permission_required("wagers.change_wager")(WagerPayoutView.as_view())),
    url(r'^wagers', WagerView.as_view(template_name="wagers/wager.html")))
