class Solution {
    public int[][] transpose(int[][] m) {
        int r=m.length,c=m[0].length,t[][]=new int[c][r];
        for(int i=0;i<r;i++)
            for(int j=0;j<c;j++)
                t[j][i]=m[i][j];
        return t;
    }
}