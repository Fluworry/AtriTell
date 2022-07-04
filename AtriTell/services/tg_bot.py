from django.conf import settings

from AtriTell.models import User

import logging
import json
import requests

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)


def process_auth_request(request):
    """
    Processes the auth tg web hook request,
    verifies that tg_auth_token in message is
    the same as in db.
    """

    request_data = json.loads(request.body)

    if request_data.get("message") is None:
        return

    message = request_data["message"]

    if message["chat"]["type"] == "private" and message["text"].startswith('/start'):
        tg_auth_token = message["text"].split(' ')[1]

        try:
            user = User.objects.filter(tg_auth_token=tg_auth_token).get()
            requests.post(f"https://api.telegram.org/bot{settings.TG_BOT_TOKEN}/sendMessage", data={
                "chat_id": message["chat"]["id"],
                "text": f"Hello, *{user.username}*!\n\n"
                        f"Now you can invite this bot to your channel, "
                        f"and the posts from AtriTell will automatically be sent to the connected channel.",
                "parse_mode": "Markdown"
            })
        except User.DoesNotExist:
            logging.error("User with this token does not exist")

    logging.debug(message)

    # if data["my_chat_member"]["new_chat_member"]["status"] == "administrator":
    #     logging.debug(data["my_chat_member"]["new_chat_member"])

