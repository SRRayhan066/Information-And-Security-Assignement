#include<bits/stdc++.h>
using namespace std;

int main(){
    char a='x';
    int temp=(int)('x'-'a')+4;
    
    temp%=26;
    char ans = 'a' + temp;
    cout<<ans<<endl;
}