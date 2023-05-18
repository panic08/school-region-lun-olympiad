#include<iostream>

using namespace std;
int main(){
    
int k;
    
int l;
    
cin >> k >> l;
    
int arr[k][l];
    
int sum[l] = {0};
   
for (int i = 0; i < k; i++){
        
	for (int j = 0; j < l; j++){
            
		cin >> arr[i][j];
        
	}
    
}
    
for (int i = 0; i < k; i++){
        
	for (int j = 0; j < l; j++){
            
		sum[j] += arr[i][j];
        
	}
    
}
 
for (int i = 0; i < l; i++){
        
	cout << sum[i] << " ";
    
}
    
return 0;

}