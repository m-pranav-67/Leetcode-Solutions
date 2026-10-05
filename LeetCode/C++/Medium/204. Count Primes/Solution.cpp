class Solution {
public:
    int countPrimes(int n){
        if (n<=2) return 0;
        int k=(n-1)/2;
        vector<bool> mrkd(k+1,false);
        for (int i=1;i<=k;i++) {
            for (int j = i; ; j++) {
                long long ind=i+j+2LL*i*j;
                if(ind > k) break;
                mrkd[ind]=true;
            }}
        int count=1;
        for (int i=1;i<=k;i++) {
            if (!mrkd[i]){
                int prime=2*i+1;
                if (prime<n) count++;
            }
        }
        return count;
    }
};