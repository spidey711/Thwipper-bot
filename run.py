from main import bot
import os

if __name__ == "__main__":
    try:
        bot.run(os.getenv("token"))
        print("Thwipper is online ;)")
    except Exception as exception:
        print(exception)