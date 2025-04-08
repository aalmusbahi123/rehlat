@echo off
cd /d %~dp0

echo ===============================
echo Pulling latest changes...
git pull --rebase

echo ===============================
echo Adding all changes...
git add .

echo ===============================
echo Committing changes...
git commit -m "push latest changes"

echo ===============================
echo Pushing to GitHub...
git push origin main

echo ===============================
echo Done! Press any key to exit.
pause
