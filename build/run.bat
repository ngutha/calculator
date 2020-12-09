if not exist "c:\run_folder" mkdir c:\run_folder
copy lib\* c:\run_folder
copy src\* c:\run_folder
python c:\run_folder\main.py