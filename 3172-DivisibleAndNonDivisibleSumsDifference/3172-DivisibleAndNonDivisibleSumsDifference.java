// Last updated: 6/4/2026, 9:42:04 PM
class Solution {
    public static int differenceOfSums(int n, int m) {
        int num1=0;
        int num2=0;
    for( int i=1;i<=n;i++){
        if(i%m==0){
            num2+=i;
        }
        else{
            num1+=i;
        }
    }
    return num1-num2;
}
public static void main(String[] args){
    int n1=10,m1=3;
    System.out.println (differenceOfSums(n1,m1));
    int n2=5,m2=6;
    System.out.println( differenceOfSums(n2,m2));
    int n3=5,m3=1;
    System.out.println( differenceOfSums(n3,m3));    
}
}