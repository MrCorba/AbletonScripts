#!/usr/bin/env bash

ABLETON_PATH="/Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts"

if [ ! -f "$ABLETON_PATH"/AbletonScripts/* ]; then
    mkdir "$ABLETON_PATH"/AbletonScripts
fi

rm -rf "$ABLETON_PATH"/AbletonScripts/*

cp ./AbletonScripts/* "$ABLETON_PATH"/AbletonScripts/
