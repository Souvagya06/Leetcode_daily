class Solution {
    public int searchInsert(int[] a, int t) {
        int l=0,h=a.length-1;
        while(l<=h){
            int m=(l+h)/2;
            if(a[m]==t) return m;
            if(a[m]<t) l=m+1;
            else h=m-1;
        }
        return l;
    }
}