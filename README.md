# pythonTestProject

 Пример тестового проекта на Python pytest + Selenium + Allure
 для просмотра отчёта должен быть установлен allure и java
 
 Для запуска тестов с созданием отчёта в allure можно запустить тесты следующими способами:

 Вариант 1. Используя в Run/Debug Configurations для поля Additional Arguments параметр: --alluredir ./results  
 
Вариант 2. В командной строке запустив команду: python -m Tests.py --alluredir ./results
 
 Для просмотра отчёта в allure команду: allure serve ./results
