#!/usr/bin/env bash

INSTALLATION_PATH=$(kpsewhich -var-value=TEXMFHOME)/tex/latex

mkdir -p $INSTALLATION_PATH
cp code-handout.sty $INSTALLATION_PATH
