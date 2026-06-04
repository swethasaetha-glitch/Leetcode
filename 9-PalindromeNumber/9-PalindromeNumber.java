// Last updated: 6/4/2026, 9:43:10 PM
class Solution {
    public boolean isPalindrome(int x) {
        
        if(x<0||(x%10==0 && x!=0)){
            return false;
        }
        int r=0;
        while(x>r){
            r=r*10+x%10;
            x/=10;
        }
        return r==x||x==r/10;
    }
}