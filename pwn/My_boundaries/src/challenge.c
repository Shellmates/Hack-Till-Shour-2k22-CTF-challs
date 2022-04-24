#include <stdlib.h>
#include <stdio.h>
#include <time.h>



//compile: gcc challenge.c -o challenge


int main(){
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

	int password=123456789;
	int random_var=55;
	int i;
	int choices[5];
	int leet=1337;
	
	srand(time(0));
	choices[0]=rand()%1000;
	choices[1]=rand()%1000;
	choices[2]=rand()%1000;
	choices[3]=rand()%1000;
	choices[4]=rand()%1000;
	
	printf("Welocome to the challenge\n===> Rules: \n   -there is 5 choices if you choose the right choice i will give you the flag.\n\n");
	printf("Choose a choice from the 5 choices: ");
	scanf("%d",&i);

	
	if(i>4){
		printf("Error: Segmantation Fault (out of my boundries)\n");
		return 0;
	}

	printf("Choice number %d == %d\n",i,choices[i]);	
	
	if(choices[i]==password){
		system("/bin/cat flag");
	}else{
		printf("Password incorrect (your choice is %d not equal the password)\n",choices[i]);
	}
	
	return 0;
}
