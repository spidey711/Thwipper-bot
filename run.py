from thwipper import bot
import os
from dotenv import load_dotenv

load_dotenv(".env")
if __name__ == "__main__":
    bot.run(os.getenv('token'))