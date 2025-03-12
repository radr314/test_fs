@echo off
echo Script started at %DATE% %TIME% > logs/script.log

:: Ensure Anaconda is activated
echo Activating Anaconda...
call "C:\Users\ranad\anaconda3\Scripts\activate.bat"


:: Change directory
echo Changing directory...
cd "C:\Users\ranad\Desktop\"

:: Activate Conda environment
echo Activating Conda environment: torch-stable
call conda activate torch-stable


:: Activate Conda environment
echo Running jupyter notebook: torch-stable
call jupyter notebook

echo Script finished at %DATE% %TIME% >> logs/script.log
