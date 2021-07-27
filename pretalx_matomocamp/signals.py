# Register your receivers here
from django.dispatch import receiver
from pretalx.agenda.recording import BaseRecordingProvider
from pretalx.cfp.signals import html_head


class MatomoVideoProvider(BaseRecordingProvider):
    def get_recording(self, submission):
        print(submission)
        return {
            "iframe": '<div class="embed-responsive embed-responsive-16by9"><iframe src="https://example.com"></iframe></div>',
            "csp_header": " …"}


# @receiver(register_recording_provider)
# def matomo_video_provider(sender, **kwargs):
#     return MatomoVideoProvider(sender)

@receiver(html_head)
def append_to_header(sender, **kwargs):
    return "<script src='/tracking.js'></script>"
