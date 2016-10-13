from bot import RespondBot
import logging
import json


if __name__ == "__main__":
    logging.basicConfig(filename='respondbot.log', level=logging.DEBUG)
    settings = json.load('settings.json')
    bot = RespondBot(settings)
    bot.run()
