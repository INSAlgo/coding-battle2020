// Solution by Louis Hasenfratz

import java.util.Scanner;
import java.util.Arrays;

public class c_niveau_audition{
	public static void main(String[] args){
		Scanner sc = new Scanner (System.in);
		int nr = sc.nextInt();
		int nspr[] = new int[nr];
		int i;
		int j;


		for(i=0;i<nr;i++){
			nspr[i]=sc.nextInt();
		}
		int np = sc.nextInt();
		int napp[] = new int[np];

		for(i=0;i<np;i++){
			napp[i]=sc.nextInt();
		}
		Arrays.sort(napp);
		boolean impossible=false;
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
						impossible=true;
						break;
					}

				}
						


			}
		}
		if (!impossible && curseur==np){

			System.out.print("POSSIBLE");
		} else {

			System.out.print("IMPOSSIBLE");
		}


	
	}

}
