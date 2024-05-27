Финальный тестовый проект SkillFactory курса QAP

Автоматизированное тестирование UI сайта: https://b2c.passport.rt.ru/ с использованием PyTest и Selenium.

С тест-кейсами можно ознакомиться по ссылке: https://docs.google.com/spreadsheets/d/1N3i-jaPSQeG3Ku87E93zkDJwDB73ivWQDkUNKg5PKVc/edit?pli=1#gid=0

В папке pages в файле main_page.py находится конструктор webdriver и общие для всех тестируемых страниц методы.

В папке pages в файлах main_page.py, recovery_page.py, passwordrecovery_page.py, registration_page.py находятся методы для соответствующих тестируемых страниц.

В папке pages в файле "locators.py находятся все локаторы.

В корне проекта в файле conftest.py находится фикстура с функцией открытия и закрытия браузера. Для запуска тестов необходимо поменять путь до webdriver на свой.

В корне проекта в файлах test_main_page.py, test_recovery_page.py, test_passwordrecovery_page.py, test_registration_page.py находятся тесты. Все тесты идут по порядку в соответствии с номерами тест-кейсов. Во всех файлах с тестами находятся закомментированные команды для запуска тестов из командной строки (# pytest -v --tb=line test_main_page.py)


