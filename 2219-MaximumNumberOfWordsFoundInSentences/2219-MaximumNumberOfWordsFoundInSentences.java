// Last updated: 6/4/2026, 9:42:19 PM
class Solution {
    public int mostWordsFound(String[] sentences) {
        int max=0;
        for( String s:sentences){
            int word=s.split(" ").length;
            max=Math.max(word,max);
        }
        return max;
    }
}