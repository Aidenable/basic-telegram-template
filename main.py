from asyncio import run

from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    from src.misc import setup
    run(setup())
