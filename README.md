# AndroidAppsDiff
This project is meant to calculate the differences between two lists of Android apps produced by the [AppListBackup](https://github.com/AndroidLabs-org/AppListBackup) app in csv format.

# Build

## Setup a python virtual environment
1. Make sure you are standing in the root of the cloned repository.
2. Create the virtual environment:
   ```bash
   python3 -m venv .venv
   ```
3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
4. Install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```