// Solution by Louis Hasenfratz

#include <stdio.h>
#include <stdlib.h>


int compare( const void* a, const void* b)
{
     int int_a = * ( (int*) a );
     int int_b = * ( (int*) b );

     if ( int_a == int_b ) return 0;
     else if ( int_a < int_b ) return -1;
     else return 1;
}


int main(){
	int nr,np;
	scanf("%d",&nr);
	int nspr[nr];
	int i;
	int j;

	for(i=0;i<nr;i++){
		scanf("%d",&nspr[i]);
	}

	scanf("%d",&np);
	int napp[np];
	for(i=0;i<np;i++){
		scanf("%d",&napp[i]);
	}

	qsort(napp , np, sizeof(int), compare );
	int impossible =0;
	int curseur=0;

	for(i=0;i<nr;i++){
		if (impossible){
			break;
		}
		if (curseur<np){
			for (j=0;j<nspr[i];j++){

				if (napp[curseur]>=i+1){
					curseur++;
					if (curseur==np){
						break;
					}
				} else {
					impossible=1;
					break;
				}

			}
						


		}
	}

	if (!impossible && curseur==np){

		printf("POSSIBLE");
	} else {

		printf("IMPOSSIBLE");
	}





}
