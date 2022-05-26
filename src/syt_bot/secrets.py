import os

from dotenv import load_dotenv


class secrets:
    DISCORD_API_KEY = None
    OPUS_PATH = None

    def __init__(self) -> None:
        load_dotenv()

        self.DISCORD_API_KEY = os.environ.get("DISCORD_API_KEY")
        assert self.DISCORD_API_KEY is not None and self.DISCORD_API_KEY != ""

        self.OPUS_PATH = os.environ.get("OPUS_PATH")
        assert self.OPUS_PATH is not None and self.OPUS_PATH != ""


SECRETS = secrets()
