from line_bot_Luis import *
from linebot.models import *
import need_to_modify as ntm
line_bot_api = LineBotApi(ntm.Channel_access_token)
handler = WebhookHandler(ntm.Channel_secret)


