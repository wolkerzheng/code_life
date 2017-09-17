#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
    public:
        int StrToInt(string str) {
            if(str.empty()){
                return 0;
            }
            int len = str.length();
            //int len1 = getStrLength("char");
           // cout<<len<<len1;
           long sum = 0;
           int s=0;
           bool flag = true;
           if(str[s]=='-') {
                flag = false;
                s++;
           }
           else if(str[s]=='+') s++;
           for(int i=s;i<len;i++)
           {
                if('0'<=str[i] && '9'>=str[i]){
                    sum = sum*10+(str[i]-48);
                }
                else
                    return 0;
           }
           if(flag)
            return sum;
            else
                return -1*sum;
        }
       int getStrLength(char *str){
            int res=0;
            if(*str == NULL){
                return res;
            }

            while(str[res]!='\0'){
                res++;
            }
            return res;
        }
};
int main()
{
    Solution s;
    cout<<s.StrToInt("-123e1");
}

/*
14 4
1 2 3 4 5 6 7 8 9 10 1 1 1 1

int main()
{
    int n,k;
    cin>>n>>k;
    vector<int> a;
    for(int i=0;i<n;i++){
        int tt;
        cin>>tt;
        a.push_back(tt);
    }
    int minG=10001;
    long sumG = 0;
    int idx = 0;
    vector<long> res;
    vector<int> tmp;
    for(int i=0;i<k;i++)
    {
        sumG+=a[i];
        tmp.push_back(a[i]);
    }

    minG = tmp[0];
    res.push_back(sumG);
    for(int i=k;i<n;i++)
    {
        if(minG<a[i])
        {
            tmp.erase(tmp.begin());
            tmp.push_back(a[i]);

            sumG = sumG - minG + a[i];
            qsort(tmp.begin(),tmp.end());
            minG = tmp[0];

        }
        res.push_back(sumG);

    }
    for(vector<long>::iterator it = res.begin();it!=res.end();it++)
    {
        cout<<*it<<' ';
    }
    cout << endl;
}*/
/*

*/
