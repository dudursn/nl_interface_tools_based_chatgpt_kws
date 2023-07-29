echo off

call .\venv\Scripts\activate

echo ...project keywords_extraction/src
cd keywords_extraction/src

if not exist ".env" (
 
 echo ...creating the env
 copy ".env.example" ".env"
 cd ..
)

echo ..
echo ..before continue we continue please check that enviroment variables in \keywords_extraction\src\.env are fulfilled
PAUSE

call flask run