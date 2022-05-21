#!/bin/bash
sudo kill -9  $(lsof -ti:8000)
uvicorn api.main:app --reload
