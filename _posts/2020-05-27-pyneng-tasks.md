---
title: "Обновление заданий и тестов книги/курса"
date: 2020-05-27
tags:
 - pyneng
category:
 - pyneng
---

В [репозитории](https://github.com/natenka/pyneng-examples-exercises) с заданиями к [курсу](https://www.youtube.com/playlist?list=PLah0HUih_ZRnJFNdZsWr2pNWgYETauGXo)/[книге](https://pyneng.readthedocs.io/) "Python для сетевых инженеров" сделано несколько изменений.

### Обновление заданий и тестов

В [репозитории с заданиями и примерами](https://github.com/natenka/pyneng-examples-exercises) кода сделано обновление:

* обновлены задания, большинство по мелочам, уточнение формулировки, приведение к одному формату
* добавлено несколько новых заданий
* обновлены тесты, больше всего разделы 25-27
* все тесты перенесены из отдельного каталога tests в каталог заданий, чтобы было меньше путанницы с тем как их запускать
* в тестах добавлено использование плагина pytest-clarity (его нужно установить `pip install pytest-clarity`) - этот плагин показывает более понятный diff при вызове теста с опцией `-vv`
* соответственно обновлены инструкции [по работе с pytest](https://pyneng.readthedocs.io/ru/latest/book/additional_info/pytest.html)
* все задания протестированы на Python 3.7 и Python 3.8

> В книге задания еще не обновлены.

Если вы уже делаете задания курса, можно клонировать репозиторий с заданиями локально и затем вручную скопировать
обновленные каталоге себе. Второй вариант - создать новый репозиторий, как написано ниже и скопировать решенные задания
в новый репозиторий.

### Шаблон репозитория

Добавлена возможность использовать репозиторий с заданиями как шаблон.
Это существенно облегчит создание своего репозитория и будет меньше нюансов при работе с заданиями.

Для создания своего репозитория на основе шаблона нужно:

-  залогиниться на [GitHub](https://github.com/)
-  открыть [репозиторий с заданиями](https://github.com/natenka/pyneng-examples-exercises)
-  нажать "Use this template" и создать новый репозиторий на основе этого шаблона
-  в открывшемся окне надо ввести название репозитория
-  после этого готов новый репозиторий с копией всех файлов из исходного репозитория с заданиями

![create repo](https://raw.githubusercontent.com/natenka/PyNEng/master/images/git/github_use_template.png)
