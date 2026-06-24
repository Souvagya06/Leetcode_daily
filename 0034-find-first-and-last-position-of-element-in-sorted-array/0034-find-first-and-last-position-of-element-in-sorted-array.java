class Solution {
    public int[] searchRange(int[] a, int t) {
        int l=0,h=a.length-1,f=-1,s=-1;
        while(l<=h){int m=(l+h)/2;
            if(a[m]>=t) h=m-1; else l=m+1;
            if(a[m]==t) f=m;
        }
        l=0; h=a.length-1;
        while(l<=h){int m=(l+h)/2;
            if(a[m]<=t) l=m+1; else h=m-1;
            if(a[m]==t) s=m;
        }
        return new int[]{f,s};
    }
}