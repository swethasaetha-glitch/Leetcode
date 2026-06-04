// Last updated: 6/4/2026, 9:42:30 PM
class Solution {
    public void reverseString(char[] s) {
        for(int i=0;i<s.length/2;i++){
            char t=s[i];
            s[i]=s[s.length-i-1];
            s[s.length-i-1]=t;
        }
    }
}