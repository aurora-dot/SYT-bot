import os

from dotenv import load_dotenv


class secrets:
    DISCORD_API_KEY = None

    def __init__(self) -> None:
        load_dotenv()

        self.DISCORD_API_KEY = os.environ.get("DISCORD_API_KEY")
        assert self.DISCORD_API_KEY is not None and self.DISCORD_API_KEY != ""


SECRETS = secrets()
