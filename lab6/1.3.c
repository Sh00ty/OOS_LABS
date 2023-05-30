#include <stdio.h>

extern char **environ;
int main(int argc, char* argv[]){
	char **p;
	int i = 0;
	for (p = environ; *p != NULL && i < 10; p++) {
		printf("%s\n", *p);
        i++;
	}
}
