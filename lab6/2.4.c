#include <stdio.h>
#include <unistd.h>

// граница на 29838
//
int main(){
	int pid = fork();
	for(int i = 0; i < 100000; ++i) {
		if(pid > 0) { printf("%d\n", i); pid = fork(); }
		else if (pid < 0) {
			printf("error making fork; i = %d\n", i);
			return 1;
		}
	}
	if(pid != 0) {
		printf("all");
	}
	sleep(15);
	return 0;
}
