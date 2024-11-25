@echo off
setlocal

for /f "delims=" %%i in ('kpsewhich -var-value=TEXMFHOME') do set INSTALLATION_PATH=%%i/tex/latex

mkdir "%INSTALLATION_PATH%"
copy code-handout.sty "%INSTALLATION_PATH%"

if not exist "%INSTALLATION_PATH%" (
   echo mkdir "%INSTALLATION_PATH%"
)

copy code-handout.sty "%INSTALLATION_PATH%"

endlocal
