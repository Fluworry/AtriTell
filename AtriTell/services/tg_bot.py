from django.conf import settings

from AtriTell.models import User, TgChannel

import logging
import json
import requests

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)


def handle_web_hook(request):
    """
    Handles telegram web hook request,
    checks its type and runs the corresponding function.
    """

    request_data = json.loads(request.body)

    if request_data.get("message"):
        handle_auth(request_data)
    elif request_data.get("my_chat_member"):
        handle_member_update(request_data)


def handle_auth(request_data):
    """
    Handles the auth request,
    verifies that tg_auth_token in message is
    the same as in db.
    """

    message = request_data["message"]

    if message["chat"]["type"] == "private" and message["text"].startswith('/start'):
        tg_auth_token = message["text"].split(' ')[1]
        user = User.objects.filter(tg_auth_token=tg_auth_token)

        if user.exists():
            requests.post(f"https://api.telegram.org/bot{settings.TG_BOT_TOKEN}/sendMessage", data={
                "chat_id": message["chat"]["id"],
                "text": f"Hello, *{user.get().username}*!\n\n"
                        f"Now you can invite this bot to your channel, "
                        f"and the posts from AtriTell will automatically be sent to the connected channel.",
                "parse_mode": "Markdown"
            })
            user.update(tg_user_id=message["from"]["id"], tg_auth_token=None)


def handle_member_update(request_data):
    """
    Adds or deletes TgChannel record
    depending on the my_chat_member_status.
    """

    my_chat_member = request_data["my_chat_member"]
    my_chat_member_status = my_chat_member["new_chat_member"]["status"]
    logging.debug(f"Status: {my_chat_member_status}")

    if my_chat_member_status == "administrator":
        TgChannel(chat_id=my_chat_member["chat"]["id"],
                  tg_user_id=User.objects.get(tg_user_id=my_chat_member["from"]["id"])).save()
        logging.debug(f'Saved new entry for TgChannel {my_chat_member["chat"]["id"]}')
    elif my_chat_member_status == "kicked":
        try:
            TgChannel.objects.get(chat_id=my_chat_member["chat"]["id"]).delete()
            logging.debug(f'Deleted TgChannel entry {my_chat_member["chat"]["id"]}')
        except TgChannel.DoesNotExist:
            logging.error("Telegram channel does not exist")

