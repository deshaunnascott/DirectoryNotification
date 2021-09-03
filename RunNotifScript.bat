@ECHO off
:: Change Directory to Notification script
TITLE Running Notification script
:: Change Directory to Notification script
cd <DIRECTORY_WITH_PYTHON_NOTIFICATION_SCRIPT>
pip install -r requirements.txt
cls
ECHO Running Notification Script ....
python Notif.py