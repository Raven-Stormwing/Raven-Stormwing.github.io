@echo on
cd /d "%~dp0"

echo Running gallery update...
python update_gallery.py

echo.
echo Finished.
pause