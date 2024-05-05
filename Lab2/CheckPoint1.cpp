#include<bits/stdc++.h>
using namespace std;

void decipher(string cipher){
    for(int i=1;i<=26;i++){
        string decipherText="";
        int val;
        for(auto ch : cipher){
            if(islower(ch)) val=ch-'a';
            else val=ch-'A';
            int tempVal=(val+i)%26;
            if(islower(ch)) decipherText+=('a'+tempVal);
            else decipherText+=('A'+tempVal);
        }
        cout<<"After Iteration "<<i<<" :: "<<decipherText<<endl;
    }
}

int main(){
    string cipher="odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo";
    cout<<"Cipher Text :: "<<cipher<<endl<<endl;
    cout<<"Deciphering ->"<<endl;
    decipher(cipher);
}