import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential
from telegram import Bot
from telegram.constants import ParseMode
from app.utils.logger import app_logger
from app.utils.message_chunker import MessageChunker


class TelegramSender:

    def __init__(self, token: str):
        self.token = token

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True
    )
    async def _send_chunk_async(self, bot: Bot, chat_id: str | int, text: str, parse_mode: str = ParseMode.MARKDOWN) -> bool:
        if not self.token or self.token in ["mock_token", "mock_ci_token"]:
            return True

        try:
            await bot.send_message(chat_id=chat_id, text=text, parse_mode=parse_mode)
            return True
        except Exception as e:
            app_logger.warning(f"Failed sending chunk with parse_mode={parse_mode}: {e}. Retrying or falling back...")
            if parse_mode == ParseMode.MARKDOWN:
                try:
                    await bot.send_message(chat_id=chat_id, text=text, parse_mode=None)
                    return True
                except Exception as ex:
                    app_logger.error(f"Fallback plain text chunk delivery failed: {ex}")
                    raise ex
            raise e

    async def send_message_async(self, chat_id: str | int, text: str, parse_mode: str = ParseMode.MARKDOWN) -> bool:
        chunks = MessageChunker.chunk_message(text, max_length=4000)
        if not chunks:
            return True

        bot = Bot(token=self.token) if (self.token and self.token not in ["mock_token", "mock_ci_token"]) else None

        for idx, chunk in enumerate(chunks, 1):
            await self._send_chunk_async(bot, chat_id, chunk, parse_mode)
            app_logger.info(f"✓ Chunk {idx} delivered")

        return True

    def send_message(self, chat_id: str | int, text: str, parse_mode: str = ParseMode.MARKDOWN) -> bool:
        return asyncio.run(self.send_message_async(chat_id, text, parse_mode))
