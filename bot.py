from flowbot import FlowBot
from flowbot.decorators import mentioned, admin_only


class RespondBot(FlowBot):
    """Respond bot can respond to a few commands."""

    def commands(self):
        return {
            '/hello': self.hello,
            '/coolio': self.coolio_lyric,
            'knock knock': self.knock_knock
        }

    @mentioned
    def hello(self, message):
        """Respond to to the message with 'Hello!'."""
        self.reply(message, "Hello!")

    @admin_only
    def coolio_lyric(self, message):
        """Respond to the message with a Coolio lyric."""
        self.reply(message, "Come on y'all let's take a ride...")

    def knock_knock(self, message):
        """Respond to 'knock knock' with 'Who's there?'."""
        self.reply(message, "Who's there?")
