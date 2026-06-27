import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential
from telegram import Bot
from telegram.constants import ParseMode
from app.utils.logger import app_logger


class TelegramSender:

    def __init__(self, token: str):
        self.token = token

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True
    )
    async def send_message_async(self, chat_id: str | int, text: str, parse_mode: str = ParseMode.MARKDOWN) -> bool:
        if not self.token or self.token in ["mock_token", "mock_ci_token"]:
            app_logger.warning("Mock token detected; skipping actual Telegram API sending.")
            return True

        bot = Bot(token=self.token)
        try:
            await bot.send_message(chat_id=chat_id, text=text, parse_mode=parse_mode)
            app_logger.info(f"Successfully sent Telegram message to chat {chat_id}.")
            return True
        except Exception as e:
            app_logger.warning(f"Failed sending message with parse_mode={parse_mode}: {e}. Retrying or falling back...")
            if parse_mode == ParseMode.MARKDOWN:
                try:
                    await bot.send_message(chat_id=chat_id, text=text, parse_mode=None)
                    app_logger.info(f"Successfully sent fallback plain text message to chat {chat_id}.")
                    return True
                except Exception as ex:
                    app_logger.error(f"Fallback plain text delivery failed: {ex}")
                    raise ex
            raise e

    def send_message(self, chat_id: str | int, text: str, parse_mode: str = ParseMode.MARKDOWN) -> bool:
        return asyncio.run(self.send_message_async(chat_id, text, parse_mode))
