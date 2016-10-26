all: install_flowbot build run

install_flowbot:
	# Remove this when flowbot becomes public, this just installs the
	# boilerplate bot alongside the respondbot so that it can be imported as if
	# it were installed.
	rm -rf flowbot
	rm -rf flowbot_tmp
	git clone git@github.com:SpiderOak/flowbot.git flowbot_tmp
	mv flowbot_tmp/src flowbot
	rm -rf flowbot_tmp

build:
	docker build -t respondbot .

run:
	docker run respondbot