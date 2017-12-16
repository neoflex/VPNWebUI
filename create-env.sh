#!/usr/bin/env bash

hash pyenv 2>/dev/null || { echo >&2 "You need to install 'pyenv' first.  Aborting."; }

pyenv install -s 3.6.3

pyenv virtualenv 3.6.3 vpngui
