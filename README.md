> Please Note: This project has not undergone a security review.


# flowbot-respondbot
This is an example of how to use the [flowbot](https://github.com/SpiderOak/flowbot) boilerplate to build bots for Semaphor.

## Run inside a Docker container
1. Make sure you have [Docker](https://www.docker.com/products/docker) installed.
2. Clone this repo: `git clone git@github.com:SpiderOak/flowbot-respondbot.git`
3. Update the `settings.json` file with your desired bot settings.
  - `username` **required**: the username of your desired bot; Semaphor usernames must be unique.  
  - `password` **required**: the password used to authenticate your bot; you will want to make sure to keep this password secure.
  - `org_id` **requred**: this is the identifier provided to you by the team admin; this is where your bot will live.
  - `display_name` *recommended*: This is the name your bot will have in the channel, (e.g. `@github`). If no display name is given, the bot will use it's username.
  - `biography`: A short description of your bot.
  - `photo`: An avatar image to use for the bot (e.g. "avatar.jpg"; must be in this directory at the time you run the `make` step below).

4. Open a terminal and navigate to this directory
5. Run the command `make` from the terminal

A docker container will be built with the `respondbot` running inside it; once the bot is up and running you should receive a join request from your bot to the team specified in the `settings.json` file. After you've accepted the join request, feel free to add the bot to any channels you'd like.


## Run Locally
If you don't want to run your bot inside a docker container, you can always run it locally:

1. Make sure you've installed [SpiderOak Semaphor](https://spideroak.com/opendownload) on your machine.
2. Clone this repo: `git clone git@github.com:SpiderOak/flowbot-respondbot.git`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `settings.json` file with your settings (see `settings.json.example` for example configuration.)
4. Run bot: `python run.py`
