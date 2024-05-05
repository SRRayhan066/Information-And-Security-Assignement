#include<bits/stdc++.h>
using namespace std;
#define ll long long

void approach1(string cipher){
    map<char,ll>freq;

    for(auto ch : cipher){
        if(isalpha(ch)){
            freq[ch]++;
        }
    }
    vector<pair<ll,char>>textFreq;
    string engFreq="etaonhisrdluwmgcfybpkvjxqz";
    for(auto it=freq.begin();it!=freq.end();it++){
        //cout<<it->first<<" "<<it->second<<endl;
        textFreq.push_back({it->second,it->first});
    }

    //cout<<endl<<endl;
    sort(textFreq.begin(),textFreq.end());
    reverse(textFreq.begin(),textFreq.end());

    map<char,char>replace; //text engText
    for(ll i=0;i<textFreq.size();i++){
        replace[textFreq[i].second]=engFreq[i];
        //cout<<textFreq[i].second<<" "<<engFreq[i]<<endl;
    }

    //cout<<endl<<endl;
    string decipher1="";

    for(auto ch : cipher){
        if(isalpha(ch)){
            decipher1+=replace[ch];
        }else decipher1+=ch;
    }

    cout<<decipher1<<endl;
}


void approach2(string cipher, string cipherKey){
    
    map<char,char>replace;
    char temp = 'a';
    for(auto ch : cipherKey){
        replace[temp++]=tolower(ch);
    }
    string decipher = "";
    for(auto ch : cipher){
        if(isalpha(ch)){
            decipher+=replace[ch];
        }else decipher+=ch;
        
    }
    cout<<decipher<<endl;
}

int main(){
    string cipher1="af p xpkcaqvnpk pfg, af ipqe qpri, gauuikifc tpw, ceiri udvk tiki afgarxifrphni cd eao- -wvmd popkwn, hiqpvri du ear jvaql vfgikrcpfgafm du cei xkafqaxnir du xrwqedearcdkw pfg du ear aopmafpcasi xkdhafmr afcd fit pkipr. ac tpr qdoudkcafm cd lfdt cepc au pfwceafm epxxifig cd ringdf eaorinu hiudki cei opceiopcaqr du cei uaing qdvng hi qdoxnicinw tdklig dvc- -pfg edt rndtnw ac xkdqiigig, pfg edt odvfcpafdvr cei dhrcpqnir--ceiki tdvng pc niprc kiopaf dfi mddg oafg cepc tdvng qdfcafvi cei kiripkqe";    
    string cipher1key = "IJTOHNDBEQRKGLMACSVWFUYPXZ";
    cout<<"Result of approaching frequecy distribution :: "<<endl<<endl;
    approach1(cipher1);
    cout<<"\nResult of using decrypt key generated from cipher breaker site :: "<<endl<<endl;
    approach2(cipher1,cipher1key);

    string cipher2 = "aceah toz puvg vcdl omj puvg yudqecov, omj loj auum klu thmjuv hs klu zlcvu shv zcbkg guovz, upuv zcmdu lcz vuwovroaeu jczoyyuovomdu omj qmubyudkuj vukqvm. klu vcdluz lu loj avhqnlk aodr svhw lcz kvopuez loj mht audhwu o ehdoe eunumj, omj ck toz yhyqeoveg auecupuj, tlokupuv klu hej sher wcnlk zog, klok klu lcee ok aon umj toz sqee hs kqmmuez zkqssuj tckl kvuozqvu. omj cs klok toz mhk umhqnl shv sowu, kluvu toz oezh lcz yvhehmnuj pcnhqv kh wovpue ok. kcwu thvu hm, aqk ck zuuwuj kh lopu eckkeu ussudk hm wv. aonncmz. ok mcmukg lu toz wqdl klu zowu oz ok scskg. ok mcmukg-mcmu klug aunom kh doee lcw tuee-yvuzuvpuj; aqk qmdlomnuj thqej lopu auum muovuv klu wovr. kluvu tuvu zhwu klok zlhhr klucv luojz omj klhqnlk klcz toz khh wqdl hs o nhhj klcmn; ck zuuwuj qmsocv klok omghmu zlhqej yhzzuzz (oyyovumkeg) yuvyukqoe ghqkl oz tuee oz (vuyqkujeg) cmubloqzkcaeu tuoekl. ck tcee lopu kh au yocj shv, klug zocj. ck czm'k mokqvoe, omj kvhqaeu tcee dhwu hs ck! aqk zh sov kvhqaeu loj mhk dhwu; omj oz wv. aonncmz toz numuvhqz tckl lcz whmug, whzk yuhyeu tuvu tceecmn kh shvncpu lcw lcz hjjckcuz omj lcz nhhj shvkqmu. lu vuwocmuj hm pczckcmn kuvwz tckl lcz vueokcpuz (ubduyk, hs dhqvzu, klu zodrpceeu-aonncmzuz), omj lu loj womg juphkuj ojwcvuvz owhmn klu lhaackz hs yhhv omjqmcwyhvkomk sowcecuz. aqk lu loj mh dehzu svcumjz, qmkce zhwu hs lcz ghqmnuv dhqzcmzaunom kh nvht qy. klu uejuzk hs kluzu, omj aceah'z sophqvcku, toz ghqmn svhjh aonncmz.tlum aceah toz mcmukg-mcmu lu ojhykuj svhjh oz lcz lucv, omj avhqnlk lcw kh ecpu ok aonumj; omj klu lhyuz hs klu zodrpceeu- aonncmzuz tuvu scmoeeg jozluj. aceah omj svhjhloyyumuj kh lopu klu zowu acvkljog, zuykuwauv 22mj. ghq loj aukkuv dhwu omj ecpu luvu,svhjh wg eoj, zocj aceah hmu jog; omj klum tu dom dueuavoku hqv acvkljog-yovkcuzdhwshvkoaeg khnukluv. ok klok kcwu svhjh toz zkcee cm lcz ktuumz, oz klu lhaackz doeeuj klucvvuzyhmzcaeu ktumkcuz auktuum dlcejlhhj omj dhwcmn hs onu ok klcvkg-klvuu";
    string cipher2key = "BXICLJYOQDTHNGAVUKFWERMZPS";
    cout<<"\n\nResult of approaching frequecy distribution :: "<<endl<<endl;
    approach1(cipher2);
    cout<<"\nResult of using decrypt key generated from cipher breaker site :: "<<endl<<endl;
    approach2(cipher2,cipher2key);
}