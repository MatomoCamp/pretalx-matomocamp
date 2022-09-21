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
        is_past_submission = submission.event == 0
        is_workshop = submission.submission_type.id == 2
        button_title = "View Workshop" if is_workshop else "View Livestream"
        livestream_url = f"https://live.matomocamp.org/" + submission.code
        chat_url = livestream_url + "/chat_room"
        recording_url = livestream_url + "/recording"
        recording_embed_url = livestream_url + "/recording_embed"
        if is_past_submission:
            return {
                "iframe": f"""
<style>
.ratio {{ margin-top:1rem}}
/* based on https://github.com/twbs/bootstrap/blob/f61a0218b36d915db80dc23635a9078e98e2e3e0/scss/helpers/_ratio.scss */
.ratio {{
    position: relative;
    width: 100%;
}}
.ratio::before {{
    display: block;
    padding-top: calc(9 / 16 * 100%);
    content: "";
}}

.ratio > * {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: none
}}
</style>
<div>
    <a href="{recording_url}" class="btn btn-primary">View Recording</a>
    <a href="{chat_url}" class="btn btn-primary">Join Chatroom</a>
</div>
<div class="ratio ratio-16x9" id="peertube-iframe">
    <iframe src="{recording_embed_url}"
            allowfullscreen
            sandbox="allow-same-origin allow-scripts allow-popups"
    ></iframe>    
</div>""",
                "csp_header": "https://video.matomocamp.org/ https://live.matomocamp.org/"
            }
        else:
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
