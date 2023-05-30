#include <stdio.h>
#include <unistd.h>
 
int main(){
    int pid = fork();
 
    if (pid == 0) {
        printf("Это сообщение из дочернего процесса\nPID: %d, PPID: %d\n", getpid(), getppid());
        sleep(3);
    }
    else {
        printf("Это сообщение из родительского процесса\nИдентификатор дочернего процесса:  %d\n", pid);
        sleep(3);
    }
 
    return 0;
}

