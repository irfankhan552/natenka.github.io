---
title: "Изменение порядка разделов в книге Python для сетевых инженеров"
date: 2020-09-14
tags:
 - pyneng
category:
 - pyneng
---

Изменение порядка разделов в книге "Python для сетевых инженеров":

1. Раздел Базы данных (18_db) перенесен в конец книги. Теперь это раздел под номером 25. Перенос связан с тем, что тема может быть сильно сложной на этом этапе изучения, плюс задания в этом разделе сложнее. Перенос темы в конец оказался очень успешным на курсе, меньше слушателей забрасывали учебу в этом месте.
2. Разделы 23, 24 по Ansible удалены, во-первых, потому что это не совсем о Python, во-вторых, потому что эти разделы теперь находятся в отдельной книге по Ansible: https://ansible-for-network-engineers.readthedocs.io/
3. Соответственно сдвинута нумерация всех остальных разделов.
4. Разделы 1-17 не менялись.



Для более плавного перехода создана копия предыдущего варианта книги. Этот вариант будет доступен до конца года.
Попасть в него можно [по ссылке](https://pyneng.readthedocs.io/ru/old_chapter_order/) или нажав в левом нижнем углу книги
на "Read the Docs" и нажать на версию  old_chapter_order (как на скриншоте).

Соответственно изменен порядок разделов [в репозитории заданий и примеров](https://github.com/natenka/pyneng-examples-exercises).
Старый порядок сохранен в ветке [old_chapter_order](https://github.com/natenka/pyneng-examples-exercises/tree/old_chapter_order).

> Все новые правки будут идти только в обновленную версию, так что лучше, по возможности, переходить на новую.

![alt]({{ site.url }}{{ site.baseurl }}/assets/images/update.png)

