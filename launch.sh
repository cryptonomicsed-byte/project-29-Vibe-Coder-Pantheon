#!/bin/bash
cd vibe-coder-pantheon
git pull
ollama serve &
python3 agents_simple.py $@ --push
