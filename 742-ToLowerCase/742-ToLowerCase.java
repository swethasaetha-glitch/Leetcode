// Last updated: 6/4/2026, 9:42:22 PM
class Solution {
    public String toLowerCase(String s) {
        String r="";
        for(int i=0;i<s.length();i++){
            char c=s.charAt(i);

            if(c>='A' && c<='Z'){
                r+=(char)(c+32);
                
            }
            else{
                r+=c;
            }
        }
        return r;
    }
}