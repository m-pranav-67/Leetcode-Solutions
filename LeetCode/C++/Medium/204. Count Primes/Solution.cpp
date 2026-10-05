class Solution {
public:
    int countPrimes(int n){
        if (n<=2) return 0;
        int k=(n-1)/2;
        vector<bool> mrkd(k+1,false);
        for (int i=1;i<=k;i++) {
            for (int j=i;j<=(k-i)/(2*i+1);j++) {
                int ind =i+j+2*i*j;
                mrkd[ind] = true;
            }}
        int count=1;
        for (int i=1; i<=k;i++) {
            if (!mrkd[i]) count++;}
        return count;
    }
};