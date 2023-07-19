#include<iostream>
#include<cstdlib>
using namespace std;
/*測量系儀器室桌上有1到9號共9台儀器，若只有其中三台未知編號的儀器有裝電池，
其他皆沒有裝，同學每次可請助教拿出或裝入三台儀器電池
(此時有電池表示為1，沒有電池表示為0)，
每次系統將提示此時有幾台儀器中裝有電池，幾台沒有 
，請用此方式，試著找出一開始就裝有電池的儀器們!*/ 
p(int i){
    int j=1;
	for(;i<2;i++){
	 j*=10;
    }
    return j;
}
int main(void){
	cout<<"測量系儀器室桌上有1到9號共九台儀器，若只有其中三台未知編號的儀器有裝電池，"<<endl; 
    cout<<"其他皆沒有裝，同學每次可請助教拿出或裝入三台儀器電池"<<endl;
    cout<<	"(此時有電池表示為1，沒有電池表示為0)，"<<endl;
    cout<<"每次系統將提示此時有幾台儀器中裝有電池，幾台沒有，"<<endl; 
    cout<<"請用此方式，試著找出一開始就裝有電池的儀器們!"<<endl;
    cout<<"(注意:儀器編號須由小到大排列)"<<endl;
	int K[1][10]={0},A,B,D,ANS=478;
	for(int j=0;j<3;j++){
    	for(int i=0;i<9;i++){
		    if(i==(ANS/p(j)-1)){
		        K[0][(ANS/p(j)-1)]=1;
	    	}
		    //cout<<endl<<K[0][i]<<endl;
	    }
		ANS=ANS%p(j); 
	}//設定ANS初始狀態 
	ANS=478; 
	do{
		cout<<"*************************************************"<<endl;
    	cout<<"您的心中是否有答案?(如果有請輸入1，沒有請輸入0):";
    	cin>>D;//D有沒有 
    	if(D==1){
    		cout<<"請輸入正確答案(請以三位數輸入):";
    		cin>>A;//A我覺得的答案 
    		if(A==ANS){
    			cout<<"恭喜你找出正確的三台儀器!"<<endl;
    		}
    		else if(A!=ANS){
			    B=0;
    		    cout<<"再接再厲!"<<endl;
    		    cout<<"請輸入你的猜測(請以三位數輸入):";
    		    cin>>A;
    		    for(int j=0;j<3;j++){
                 	for(int i=0;i<9;i++){
		                 if(i==(A/p(j)-1)){
		                     K[0][(A/p(j)-1)]=!(K[0][(A/p(j)-1)]);
	    	             }
		              //cout<<endl<<K[0][i]<<endl;
	                }
	         	    A=A%p(j); 
	            }//設定A初始狀態
    		    for(int j=0;j<9;j++){
    		        B+=K[0][j];
	        	}
	    	cout<<B<<"台有裝電池"<<(9-B)<<"台沒裝電池"<<endl;
    		}	
    	}
    	else if(D==0){
		        B=0;
    		    cout<<"再接再厲!"<<endl;
    		    cout<<"請輸入你的猜測(請以三位數輸入):";
    		    cin>>A;
    		    for(int j=0;j<3;j++){
                 	for(int i=0;i<9;i++){
		                 if(i==(A/p(j))-1){
		                     K[0][(A/p(j)-1)]=!(K[0][(A/p(j)-1)]);
	    	             }
	                }
	         	    A=A%p(j); 
	            }//設定A初始狀態
    		    for(int j=0;j<9;j++){
    		        B+=K[0][j];
	        	}
	    	cout<<B<<"台有裝電池"<<(9-B)<<"台沒裝電池"<<endl;	
    	}
    }while(A!=ANS);
}


	
	
	


