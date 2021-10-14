# Register your receivers here
from django.dispatch import receiver
from pretalx.agenda.recording import BaseRecordingProvider
from pretalx.agenda.signals import register_recording_provider
from pretalx.cfp.signals import html_head
from pretalx.submission.models import Submission


class MatomoVideoProvider(BaseRecordingProvider):
    """
    a bit of a hack to add buttons linking to livestream and chat to the details page
    """

    def get_recording(self, submission: Submission):
        is_workshop = submission.submission_type.name == "Workshops"
        button_title = "View Workshop" if is_workshop else "View Livestream"
        livestream_url = f"https://live.matomocamp.org/" + submission.code
        chat_url = livestream_url + "/chat_room"
        return {
            "iframe": f"""
            <div>
            <a href='{livestream_url}' class='btn btn-primary'>{button_title}</a>
            <a href="{chat_url}" class="btn btn-primary">Join Chatroom</a>
            </div>
            """,
        }


@receiver(register_recording_provider)
def matomo_video_provider(sender, **kwargs):
    return MatomoVideoProvider(sender)


@receiver(html_head)
def append_to_header(sender, **kwargs):
    return "<script src='/tracking.js'></script>"
