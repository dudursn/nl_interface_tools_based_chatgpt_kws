echo off

call .\venv\Scripts\activate

echo ...project app/src
cd app/src

if not exist ".env" (
 
 echo ...creating the env
 copy ".env.example" ".env"
 cd ..
)

echo ..
echo ..before continue we continue please check that enviroment variables in \app\src\.env are fulfilled
PAUSE

call python main.py kws