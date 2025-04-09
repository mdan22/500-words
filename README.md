# 500 Words Challenge

A simple automation tool that creates a new markdown file each day for a daily writing challenge.

## Overview

This project helps maintain a daily writing habit by automatically generating a new markdown file at first login each day. It's designed to eliminate the friction of creating and naming files, allowing you to focus solely on writing.

The writings can be easily backed up through github.

## How It Works

1. At the first Windows login of the day, the Task Scheduler triggers a batch script
2. The script runs a Python program through WSL (Windows Subsystem for Linux)
3. The program checks if a file was already created today
4. If not, it creates a new markdown file with the proper day number
5. The new file opens in VS Code automatically, ready for your 500 words

## Setup

### Prerequisites
- Windows with WSL (Ubuntu) installed
- VS Code on WSL
- Python 3.x on WSL
- Windows Task Scheduler

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/mdan22/500-words-challenge.git
   ```

2. Configure Task Scheduler:
   - Open Windows Task Scheduler
   - Create a new task to run at user login
   - Set the action to run `scripts/run_daily_writing.bat`
   - Set the "Start in" directory to your repository location

## Project Structure

- `scripts/`: Contains the Python script and batch file for automation
- `writing/`: Contains daily writing markdown files

## Backup and Version Control
The project can even be used to back up writings seamlessly through Github.

## License

MIT License - See LICENSE file for details