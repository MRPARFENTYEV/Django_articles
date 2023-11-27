 в терминале переходим в папку: cd m2m-relations
 устанавливаем sql: pip install Django[sqlite3] хотя пишет что уже сделано
 загружаем статьи: python manage.py loaddata articles.json
 создаем миграции: python manage.py makemigrations   
 применяем миграции: python manage.py migrate(судя по некоторым источникам 4 строчку можно пропустить,
 но я всеравно выполняю)      
 далее команды из документации докера на создание и запуск контейнера:
 docker build -t urlshortener . 
 docker run -p 8000:8000 -t urlshortener
