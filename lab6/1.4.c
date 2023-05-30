#include <stdio.h>
#include <stdlib.h>

extern char **environ;
int main(int argc, char* argv[]){
	if(argc < 2) {
		printf("Usage: %s <number of vars>\n", argv[0]);
		return 1;
	}
	char **p;
	int i = 0;
	int max = atoi(argv[1]);
	if(max < 0) {
		printf("number must be >= 0\n");
		return 1;
	}
	for (p = environ; *p != NULL && i < max; p++) { 
		printf("%s\n", *p);
		i += 1;
	}
}
