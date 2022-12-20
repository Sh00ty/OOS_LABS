- Что происходит при прерывании скрипта text-trap.sh? Объясните, почему.
```
Происходит перехват сигнала SIGINT (SIGNAL INTERRUPT), и перед экстренным завершинем программы происходит вызов обработчика, выполняющего в данном случае следующий скрипт 'echo "Аварийное завершение..."; exit 1'
```
- Напишите, по какой причине выводы команды ls -l /proc/self и ls -l /proc/$$ отличаются?
```
Файл /proc/self является символической ссылкой, и его содержимое меняется в зависимости от того, кто к ней обращается. 
Вывод команды `ls -l /proc/self` соответствует идентификатору процесса ls.

$$ — переменная bash, определяющая pid текущего процесса(скрипта). 
Вывод команды `ls -l /proc/$$` соответствует pid оболочки bash.
```
- Напишите, какие дескрипторы в выводе команды ls -l /proc/self/fd отвечают за stdin, stdout, stderr.
```
stdin  - 0
stdout - 1
stderr - 2
```
- Что происходит с дескрипторами при перенаправлении потоков stdout и stderr в файлы при выполнении команды ls -l /proc/self/fd > /tmp/ls.out 2> /tmp/ls.err?
```
Происходит переназначение файловых дескрипторов для потоков вывода и ошибок.
Потоки вывода и ошибок перенаправляются в файлы /tmp/ls.out и /tmp/ls.err соответственно.
```
- Запишите эту же команду, добавив к ней перенаправление потока stdin. Что изменилось?
```
ls -l /proc/self/fd < /tmp/ls.in > /tmp/ls.out 2> /tmp/ls.err
Если данный файл существует, то вывод будет записан в ls.out, иначе в tmp/ls.err будет записано, что данного файла не существует    
```
- Какой эффект наблюдается при выполнении команды exec ps -l?
```
Текущий процесс оболочки заменяется процессом команды ps -l, вывод записывается в stdout, после чего процесс оболочки заершается.
```
- Что означает pos при выводе содержимого файла /proc/$$/fdinfo/3?
```
Это позиция указателя чтения-записи в открытом файле процесса оболочки Bash.
```
- Существует ли возможность читать содержимое файла test.out даже после его удаления? Почему так происходит?
```
Удаление файла — это удаление указателя на его иноду и удаление содержимого файла, если не остается ни одной жесткой ссылки на него.

В случае, если обращение к файлу test.out осуществляется через дескриптор, вывод команды `cat <&4` должен быть пустым: файловый дескриптор указывает на иноду файла, который существует после удаления данного файла.

При обращении к файлу test.out по имени выводится сообщение об ошибке.
```