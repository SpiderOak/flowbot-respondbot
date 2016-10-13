from bot import RespondBot
import logging
import json


if __name__ == "__main__":
    logging.basicConfig(filename='respondbot.log', level=logging.DEBUG)

    with open('settings.json') as data_file:
        settings = json.load(data_file)

    bot = RespondBot(settings)
    bot.run()
