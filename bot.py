from aiohttp import web
from plugins import web_server
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, FORCE_SUB_CHANNEL, CHANNEL_ID, PORT
import pyrogram.utils

# Set minimum values for chat and channel IDs to avoid Pyrogram warnings
pyrogram.utils.MIN_CHAT_ID = -999999999999
pyrogram.utils.MIN_CHANNEL_ID = -100999999999999

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        # Force subscription channel setup
        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as e:
                self.LOGGER(__name__).warning(f"Error with FORCE_SUB_CHANNEL: {e}")
                self.LOGGER(__name__).warning("Please ensure bot is admin with 'Invite Users via Link' permission.")
                self.LOGGER(__name__).info("Bot Stopping. Contact support if needed.")
                sys.exit()

        # Database channel setup
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test_message = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test_message.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(f"Error with CHANNEL_ID: {e}")
            self.LOGGER(__name__).warning("Ensure bot is admin in DB channel and CHANNEL_ID is correct.")
            self.LOGGER(__name__).info("Bot Stopping. Contact support if needed.")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info("Bot is now running.")
        self.LOGGER(__name__).info("Created by https://t.me/ultroid_official")
        
        # Web server for HTTP interactions
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
