#include<iostream>
#include<cstdlib>
using namespace std;
/*���q�t�����Ǯ�W��1��9���@9�x�����A�Y�u���䤤�T�x�����s�����������˹q���A
��L�ҨS���ˡA�P�ǨC���i�ЧU�Ю��X�θˤJ�T�x�����q��
(���ɦ��q����ܬ�1�A�S���q����ܬ�0)�A
�C���t�αN���ܦ��ɦ��X�x�������˦��q���A�X�x�S�� 
�A�ХΦ��覡�A�յۧ�X�@�}�l�N�˦��q����������!*/ 
p(int i){
    int j=1;
	for(;i<2;i++){
	 j*=10;
    }
    return j;
}
int main(void){
	cout<<"���q�t�����Ǯ�W��1��9���@�E�x�����A�Y�u���䤤�T�x�����s�����������˹q���A"<<endl; 
    cout<<"��L�ҨS���ˡA�P�ǨC���i�ЧU�Ю��X�θˤJ�T�x�����q��"<<endl;
    cout<<	"(���ɦ��q����ܬ�1�A�S���q����ܬ�0)�A"<<endl;
    cout<<"�C���t�αN���ܦ��ɦ��X�x�������˦��q���A�X�x�S���A"<<endl; 
    cout<<"�ХΦ��覡�A�յۧ�X�@�}�l�N�˦��q����������!"<<endl;
    cout<<"(�`�N:�����s�����Ѥp��j�ƦC)"<<endl;
	int K[1][10]={0},A,B,D,ANS=478;
	for(int j=0;j<3;j++){
    	for(int i=0;i<9;i++){
		    if(i==(ANS/p(j)-1)){
		        K[0][(ANS/p(j)-1)]=1;
	    	}
		    //cout<<endl<<K[0][i]<<endl;
	    }
		ANS=ANS%p(j); 
	}//�]�wANS��l���A 
	ANS=478; 
	do{
		cout<<"*************************************************"<<endl;
    	cout<<"�z���ߤ��O�_������?(�p�G���п�J1�A�S���п�J0):";
    	cin>>D;//D���S�� 
    	if(D==1){
    		cout<<"�п�J���T����(�ХH�T��ƿ�J):";
    		cin>>A;//A��ı�o������ 
    		if(A==ANS){
    			cout<<"���ߧA��X���T���T�x����!"<<endl;
    		}
    		else if(A!=ANS){
			    B=0;
    		    cout<<"�A���A�F!"<<endl;
    		    cout<<"�п�J�A���q��(�ХH�T��ƿ�J):";
    		    cin>>A;
    		    for(int j=0;j<3;j++){
                 	for(int i=0;i<9;i++){
		                 if(i==(A/p(j)-1)){
		                     K[0][(A/p(j)-1)]=!(K[0][(A/p(j)-1)]);
	    	             }
		              //cout<<endl<<K[0][i]<<endl;
	                }
	         	    A=A%p(j); 
	            }//�]�wA��l���A
    		    for(int j=0;j<9;j++){
    		        B+=K[0][j];
	        	}
	    	cout<<B<<"�x���˹q��"<<(9-B)<<"�x�S�˹q��"<<endl;
    		}	
    	}
    	else if(D==0){
		        B=0;
    		    cout<<"�A���A�F!"<<endl;
    		    cout<<"�п�J�A���q��(�ХH�T��ƿ�J):";
    		    cin>>A;
    		    for(int j=0;j<3;j++){
                 	for(int i=0;i<9;i++){
		                 if(i==(A/p(j))-1){
		                     K[0][(A/p(j)-1)]=!(K[0][(A/p(j)-1)]);
	    	             }
	                }
	         	    A=A%p(j); 
	            }//�]�wA��l���A
    		    for(int j=0;j<9;j++){
    		        B+=K[0][j];
	        	}
	    	cout<<B<<"�x���˹q��"<<(9-B)<<"�x�S�˹q��"<<endl;	
    	}
    }while(A!=ANS);
}


	
	
	


