#include<bits/stdc++.h>
using namespace std;

int main(){
    string hash1,hash2;
    cin>>hash1>>hash2;
    int result = 0;
    for(int i=0;i<hash1.size();i++){
        if(hash1[i]==hash2[i]) result++;
    }
    cout<<"Matched Bit : "<<result<<endl;
    return 0;
}