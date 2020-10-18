// Solution by Louis Hasenfratz

import java.util.Scanner;

public class a_tickets{
	public static void main(String[] args){
		Scanner sc = new Scanner (System.in);
		int n = sc.nextInt();
		int p1=sc.nextInt();
		int p2=sc.nextInt();
		int p3=sc.nextInt();
		if (n>200){
			n=n-200;
			System.out.println(n*p3+100*p2+100*p1);
		} else if (n>100){
			n=n-100;
			System.out.println(n*p2+100*p1);
		} else{
			
			System.out.println(n*p1);
		} 


	
	}

}
