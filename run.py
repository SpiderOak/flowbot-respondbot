from bot import RespondBot
import logging


if __name__ == "__main__":
    logging.basicConfig(filename='respondbot.log', level=logging.DEBUG)

    bot = RespondBot()
    bot.run()
