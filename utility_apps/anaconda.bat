@echo off
echo Script started at %DATE% %TIME% > logs/script.log

:: Ensure Anaconda is activated
echo Activating Anaconda... >> script.log 2>&1
call "C:\Users\ranad\anaconda3\Scripts\activate.bat" >> logs/script.log 2>&1


:: Change directory
echo Changing directory... >> logs/script.log 2>&1
cd "C:\Users\ranad\Desktop\"

:: Activate Conda environment
echo Activating Conda environment: torch-stable >> logs/script.log 2>&1
call conda activate torch-stable >> logs/script.log 2>&1


:: Activate Conda environment
echo Running jupyter notebook: torch-stable >> logs/script.log 2>&1
jupyter notebook

echo Script finished at %DATE% %TIME% >> logs/script.log
