Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).

grep '.*' /etc/passwd | cut -d ':' -f 1 | sort
![image](https://github.com/user-attachments/assets/475937e7-9df1-41f9-96c8-0def095bbf3a)

Задача 2
Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов, как показано в примере ниже:

[root@localhost etc]# cat /etc/protocols ...
142 rohc
141 wesp
140 shim6
139 hip
138 manet

cat /etc/protocols | awk '{print $2, $1}' | sort -nr | head -5
![image](https://github.com/user-attachments/assets/daec406d-3254-4501-a133-cff5a561b3ce)


Задача 3
Написать программу banner средствами bash для вывода текстов, как в следующем примере (размер баннера должен меняться!):

[root@localhost ~]# ./banner "Hello from RTU MIREA!"
+-----------------------+
| Hello from RTU MIREA! |
+-----------------------+
Перед отправкой решения проверьте его в ShellCheck на предупреждения.

![image](https://github.com/user-attachments/assets/a8510479-8b1c-45d7-839a-3af4cf2fc64b)

![image](https://github.com/user-attachments/assets/6abe41b6-515c-441a-afbb-2de13e7465c9)


Задача 4
Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).

Пример для hello.c:

h hello include int main n printf return stdio void world

![image](https://github.com/user-attachments/assets/87219082-dbf5-433a-ac03-e0c2313c8b3e)


![image](https://github.com/user-attachments/assets/9818ab50-bdaa-4066-9f1f-1f449b0f0db5)

Задача 5
Написать программу для регистрации пользовательской команды (правильные права доступа и копирование в /usr/local/bin).

Например, пусть программа называется reg:

./reg banner
В результате для banner задаются правильные права доступа и сам banner копируется в /usr/local/bin.

![image](https://github.com/user-attachments/assets/a07e9fb2-a50b-453a-8627-fe0ae0c17aa2)


![image](https://github.com/user-attachments/assets/1f64ef86-0ec6-4e68-a7c3-e189c2bd9b82)


Задача 6
Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.
![image](https://github.com/user-attachments/assets/016e6eee-ee44-43f3-a427-b0c2607d0be5)

![image](https://github.com/user-attachments/assets/f5903435-bb55-46ee-903f-b89a93026adc)


Задача 7
Написать программу для нахождения файлов-дубликатов (имеющих 1 или более копий содержимого) по заданному пути (и подкаталогам).

#!/bin/bash

directory="$1"

# Поиск дубликатов с использованием md5sum
find "$directory" -type f -print0 | xargs -0 md5sum | sort | uniq -d -w 32 | sed -r 's/^[0-9a-f]*( )//' | while read -r duplicate; do
  echo "Дубликат: $duplicate"
  
Задача 8
Написать программу, которая находит все файлы в данном каталоге с расширением, указанным в качестве аргумента и архивирует все эти файлы в архив tar.

extension="$1"
archive_name="$2"

files=$(find . -type f -name "*.$extension")

tar -czvf "$archive_name.tar.gz" $files

echo "Завершено!"

Задача 9
Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.
input_file="$1"
output_file="$2"
sed 's/    /\t/g' "$input_file" > "$output_file"
echo "Завершено!"



Задача 10
Написать программу, которая выводит названия всех пустых текстовых файлов в указанной директории. Директория передается в программу параметром.
#!/bin/bash

directory="$1"
find "$directory" -type f -empty -exec file {} \; | grep "empty" | cut -d: -f1
