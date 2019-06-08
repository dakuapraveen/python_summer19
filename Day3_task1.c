#include<stdio.h>
#include<stdlib.h>
void main()
{
	FILE *fptr;
	char filename[20], ch;
	int count=0;
	printf("enter the file name");
	scanf("%s",&filename);
	fptr=fopen(filename,"r");
	ch=fgetc(fptr);
	while(ch != EOF)
	{
		if(ch=='\n')
		{
			count=count+1;
		}
		ch=fgetc(fptr);
	}
	fclose(fptr);
	print("lines=%d",count);
}
