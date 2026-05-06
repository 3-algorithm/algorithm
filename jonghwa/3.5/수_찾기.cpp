#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin>>n;

    vector<int> v1(n);

    for (int i=0;i<n;++i){
        cin>>v1[i];
    }
    
    sort(v1.begin(),v1.end());
    
    int m;
    cin>>m;

    for (int i=0;i<m;++i){
        int a;
        cin>>a;
        //처음과 끝을 탐색하고,a가 있으면 true 반환
        if (binary_search(v1.begin(),v1.end(),a)){
            cout<<1<<"\n";
        }
        else {
            cout<<0<<"\n";
        }
    }
        
    
    return 0;
}