@echo off
cd %~dp0
wsl -e bash -ic "cd $(wslpath '%~dp0') && python3 create_daily_file.py"