# flowbot-respondbot
This is an example of how to use the flowbot-barebones boilerplate to build bots for Semaphor.

## Install
Make sure you've installed Semaphor, `flow-python`, and `flowbot-barebores`
```
pip install git+git://github.com/SpiderOak/flow-python.git@master
pip install git+git://github.com/SpiderOak/flowbot-barebones.git@master
```

> NOTE: While this is a private repo you will need to use `git+ssh`
```
pip install git+ssh://git@github.com/SpiderOak/flowbot-barebones.git@master
```

## Settings
Currently, settings are read directly from environment variables. You can change
them by editing the `run.sh` script file.

## Running
```
python run.py
```