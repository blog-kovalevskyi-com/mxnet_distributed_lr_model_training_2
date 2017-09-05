#!/bin/bash
python server.py &
python scheduler.py &
python worker1.py &
python worker2.py
