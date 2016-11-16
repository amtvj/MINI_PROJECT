#include <bits/stdc++.h>
using namespace std;

int main(){
	FILE *fp = fopen("ACCEDEranking.txt","r");
	FILE *fp1 = fopen("valence.txt","w");
	FILE *fp2 = fopen("arousal.txt","w");
	int id,vrank,arank;
	double vvalue,avalue,vvar,avar;
	char name[100];
	while(fscanf(fp,"%d      %s	%d	%d	%lf	%lf	%lf	%lf\n",&id,name,&vrank,&arank,&vvalue,&avalue,&vvar,&avar) != EOF){
		fprintf(fp1,"%lf\n",vvalue);
		fprintf(fp2,"%lf\n",avalue);
		//fscanf(fp,"%d      %s	%d	%d	%f	%f	%f	%f\n",&id,name,&vrank,&arank,&vvalue,&avalue,&vvar,&avar);
	}
	fclose(fp);
	fclose(fp1);
	fclose(fp2);
}