@echo off
REM IMPORTANT!: You have to run this code as an administrator!

REM Fetch the latest Python version
for /f %%i in ('powershell -command "(Invoke-WebRequest -Uri 'https://endoflife.date/api/python.json').Content | ConvertFrom-Json | Where-Object { $_.latest } | Select-Object -ExpandProperty latest"') do set "latest_py_version=%%i"

echo Latest Python version: %latest_py_version%

REM Check if Python is installed and up to date
for /f "tokens=2" %%v in ('python --version 2^>^&1') do set "current_version=%%v"
if not defined current_version (
    echo Python not installed. Proceeding with installation.
) else (
    if "%current_version%" geq "%latest_py_version%" (
        echo Python %latest_py_version% or greater is already installed. Exiting.
        exit /b
    )
)

REM Download and install Python
set "installer=python-%latest_py_version%-amd64.exe"
set "targetdir=C:\Python%latest_py_version%"
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/%latest_py_version%/%installer%', '%installer%')"

start /wait %installer% /quiet /passive InstallAllUsers=1 TargetDir=%targetdir%

REM Add Python to the system PATH
setx PATH "%targetdir%;%PATH%" /M

REM Cleanup
del %installer%
echo Python %latest_py_version% installed and added to the system PATH.

pause

REM Installing PyQt5

pip install PyQt5
