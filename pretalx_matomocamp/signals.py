# Register your receivers here
from django.dispatch import receiver
from pretalx.agenda.signals import register_recording_provider
from pretalx.cfp.signals import html_head
from pretalx.agenda.recording import BaseRecordingProvider


class MatomoVideoProvider(BaseRecordingProvider):
    def get_recording(self, submission):
        print(submission)
        return {"iframe": '<div class="embed-responsive embed-responsive-16by9"><iframe src="https://example.com"></iframe></div>', "csp_header": " …"}


# @receiver(register_recording_provider)
# def matomo_video_provider(sender, **kwargs):
#     return MatomoVideoProvider(sender)

@receiver(html_head)
def append_to_header(sender,**kwargs):
    return """<!-- Matomo -->
<script type="text/javascript">
  var _paq = window._paq = window._paq || [];
  /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
  _paq.push(["disableCookies"]);
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="//mtm.matomocamp.org/";
    _paq.push(['setTrackerUrl', u+'matomo.php']);
    _paq.push(['setSiteId', '3']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript'; g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
  })();
</script>
<!-- End Matomo Code -->"""
