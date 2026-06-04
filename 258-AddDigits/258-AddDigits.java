// Last updated: 6/4/2026, 9:42:34 PM
class Solution {
    public int addDigits(int num) {
        while(num>=10){
        int s=0;
        while(num>0){
            int d=num%10;
            s+=d;
            num/=10;
        }
        num=s;
        }
        return num;
    }
}