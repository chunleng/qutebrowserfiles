#!/usr/bin/env bash

set eu

APP_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" && pwd  )"

# install vimrc
mkdir -p $HOME/.qutebrowser
mkdir $HOME/.qutebrowser/bookmarks
ln -sfn ${APP_PATH}/bookmarks/urls $HOME/.qutebrowser/bookmarks.base
ln -sfn ${APP_PATH}/src $HOME/.qutebrowser
ln -sfn ${APP_PATH}/js $HOME/.qutebrowser
ln -sfn ${APP_PATH}/greasemonkey $HOME/.qutebrowser
ln -sfn ${APP_PATH}/config.py $HOME/.qutebrowser
ln -sfn ${APP_PATH}/quickmarks $HOME/.qutebrowser/quickmarks.base
ln -sfn ${APP_PATH}/userscripts $HOME/.qutebrowser
