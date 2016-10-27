all: build run

build:
	docker build -t respondbot .

run:
	docker run respondbot