Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).

grep '.*' /etc/passwd | cut -d ':' -f 1 | sort
![image](https://github.com/user-attachments/assets/475937e7-9df1-41f9-96c8-0def095bbf3a)
