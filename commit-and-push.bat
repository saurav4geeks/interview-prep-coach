@echo off
cd /d "%~dp0"
echo Setting remote origin...
git remote remove origin 2>nul
git remote add origin https://github.com/saurav4geeks/interview-prep-coach.git
echo.
echo Pushing to main...
git push -u origin main
echo.
echo Done! Check above for any errors.
pause
