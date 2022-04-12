# test_yandex
Проект тестирования страниц Яндекса
____
## Используемые модули:
```
selenium, pytest
```
## Установки
Тестирование происходит при помощи веб драйвера — программы, которая позволяет взаимодействовать с браузером Google Chrome при помощи Selenium.
Я использую браузер Google Chrome, так как на данный момент это самый популярный браузер, и в первую очередь следует убедиться, что веб-приложение работает для большинства пользователей.
Драйвер для Chrome разрабатывается командой браузера и носит название ChromeDriver. Скачать нужную версию можно с официального сайта по ссылке:
https://chromedriver.chromium.org/

### Установка на Windows
+ Создайте на диске C: папку chromedriver и положите разархивированный ранее файл chromedriver.exe в папку C:\chromedriver.
+ Добавьте в системную переменную PATH папку C:\chromedriver. Как это сделать в разных версиях Windows, описано здесь: https://www.computerhope.com/issues/ch000549.htm. 

### Установка на Linux
+ Распакуйте скачанный драйвер
```
unzip chromedriver_linux64.zip
```
+ Переместите разархивированный файл с СhromeDriver в нужную папку и разрешите запускать chromedriver как исполняемый файл:
```
sudo mv chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver
```
