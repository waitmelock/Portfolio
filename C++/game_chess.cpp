#include<iostream>
#include<stdio.h> 
#include<cstdlib>
//�y���� 
//�W�h:�Ъ��a��ܱ�����ߤl(�HR���)���y��(�HD���)�A�Ѿ���ߤl�����a�}�l�A���y��J�Q�n�e������m�y�СA
//�a�Ϥήy�Цp�U�ϩҥܡA�ߤl�ѥk��}�l�A�T���y���N�󥪤�}�l�A�a�ϳs�����u�q�����I�i�H�e������V 
//��J�y�Юɶ��`�N�y�����i���^�Y���A�]�N�O���੹���貾�ʡA�@���u�ಾ�ʤ@���y���A�B�u�ಾ�ʤ@�B�A 
//�Өߤl�C���i�H���|�P���N�@�����q���D�����ʤ@�B�A�H�����y�����]��A
//��ߤl���\�k���c�����]��è�F�y��(1,0)�ɡA�ߤl����ӡA�Ϥ��A
//�Y�y���̦��\�Ϩߤl�L���i�k�A�h���y����ӡC 
//�`�N:��J�y�ЮɽХH(x�ťի�y)���覡��J
//�A�Y��J�y��(0,0)(0,4)(2,0)(2,4)�z�N�|�^�J�¬}���A�æ^���Ӫ���m�C 

using namespace std;
//��X�ѽL
void checker(char b[3][5]){
	for(int i=0;i<3;i++){	
	    if(i==0||i==2){
			cout<<" ";
		}
		for(int j=0;j<5;j++){
			cout<<b[i][j];
			if(j==1||j==2||(i==1&&j==3)||(i==1&&j==0)){
			    cout<<"-";
			}
	    }
		cout<<endl;
		if(i==0){
			cout<<" /|\\|/|\\ "<<endl;
		}
		if(i==1){
			cout<<" \\|/|\\|/ "<<endl;
		}	
	}
} 

int main(void){
	int aR=1,bR=4;//�ߤl�e�i�y��
	int cR,dR;//�ߤl��l�y�� 
	int aD,bD;//�y���e�i�y��
	int cD,dD;//�y����l�y��
	int k=0;//�n���n�~��j�� 
	char s;//�ѽL�����F�褬�� 
	char ma[3][5]={};
	//��l�� 
	for(int i=0;i<=2;i++){
		for(int j=0;j<=4;j++){
			ma[i][j]='O';
			if((i==0&&j==0)||(i==0&&j==4)||(i==2&&j==0)||(i==2&&j==4)){
			    ma[i][j]=' ';
			}
			
		}
	}
	ma[1][4]='R';	
	ma[0][1]='D';
	ma[1][0]='D';
	ma[2][1]='D';
	cout<<"�y����"<<endl; 
    cout<<"�W�h:�Ъ��a��ܱ�����ߤl(�HR���)���y��(�HD���)�A�Ѿ���ߤl�����a�}�l�A"<<endl;
	cout<<"���y��J�Q�n�e������m�y�СA�a�Ϥήy�Цp�U�ϩҥܡA�ߤl�ѥk��}�l�A�T���y��"<<endl;
	cout<<"�N�q����}�l�A�a�ϳs�����u�q�����I�i�H�e������V�A��J�y�Юɶ��`�N�y�����i"<<endl;
	cout<<"���^�Y���A�]�N�O���੹����(���B���U�B���W)���ʡA�@���u�ಾ�ʤ@���y���A�B�u"<<endl; 
	cout<<"�ಾ�ʤ@�B�A�Ө�";
	cout<<"�l�C���i�H���|�P���N�@�����q���D�����ʤ@�B�A�H�����y�����]��A��ߤl���\\�k"<<endl; 
	cout<<"���y�����]��è�F�y��(1,0)�ɡA�ߤl����ӡA�Ϥ��A�Y�y���̦��\\�Ϩߤl�L���i�k"<<endl; 
	cout<<"�h���y����ӡC"<<endl;
    cout<<"�`�N:��J�y�ЮɽХH(x�ť���y)���覡��J�A�Y��J�W�h�~���y�СA�z�N�|�^�J"<<endl; 
	cout<<"�¬}���A�æ^���Ӫ���m"<<endl; 
	
	//�a��
	cout<<"�a��:"<<endl;
	checker(ma);
	//�y�� 
	cout<<"�y��:"<<endl;
	for(int i=0;i<3;i++){	
	    if(i==0||i==2){
			cout<<"      ";
		}
		for(int j=0;j<5;j++){
		    if((i==0&&j==0)||(i==0&&j==4)||(i==2&&j==0)||(i==2&&j==4)){
		        continue;
			}
			else{
				cout<<"("<<i<<","<<j<<")";
			}
			
			if(j==1||j==2||(i==1&&j==3)||(i==1&&j==0)){
			    cout<<"-";
			}
	    }
		cout<<endl;
		if(i==0){
			cout<<"     /  |  \\  |  /  |  \\ "<<endl;
		}
		if(i==1){
			cout<<"     \\  |  /  |  \\  |  / "<<endl;
		}	
	}
	cout<<endl;
	
	//game start
	while(0==0){
	//�ߤl��J 	
	cR=aR;
	dR=bR;
	cout<<"�Ъ��a��J�ߤl�n�e�����y��:";
	do{
	    cin>>aR>>bR;
		k=0;
	    //���b�P�_�i���i�H��J�y�� 
	    if((aR==0&&(bR>3||bR<1))||(aR==1&&(bR<0||bR>4))||(aR==2&&(bR>3||bR<1))||(aR>=3)){
		    cout<<"�z���ߤl���i�¬}�̰�!"<<endl;
		    cout<<"�Э��s��J���e�����y��:";
		    k=1;
			continue;
		    
	    }
		//���ਫ�W�L�@��
		if(((aR!=cR)&&(aR!=(cR+1))&&(aR!=(cR-1)))||((bR!=dR)&&(bR!=(dR+1))&&(bR!=(dR-1)))){
			cout<<"�@���u�ਫ�@���!"<<endl;
			cout<<"�Э��s��J���e�����y��:";
    		k=1;
			continue;
		}
		//�������q 
		if((((cR==1&&dR==1)||(cR==1&&dR==3))&&(aR==0||aR==2)&&bR==2)||(((cR==0&&dR==2)||(cR==2&&dR==2))&&(aR==1||aR==3)&&aR==1)){
			cout<<"�������q!"<<endl;
			cout<<"�Э��s��J���e�����y��:";
    		k=1;
			continue;
		} 
		//���b:����ݦb�������
		if(aR==cR&&bR==dR){
			cout<<"���௸�b��a���ʳ�!"<<endl;
			cout<<"�Э��s��J���e�����y��:";
    		k=1; 
			continue;
		}
	    //���b�P�_�o�@��O���O�y�� 
	    if(ma[aR][bR]=='D'){
	 	    cout<<"�֧�A���ߤl�a���A�_�h�n�Q�y���Y����!"<<endl;
	    	cout<<"�Э��s��J���e�����y��:";
	    	k=1;
			continue;
	    }
	    
	   
		   
    }while(k==1);
    k=ma[cR][dR];
    ma[cR][dR]=ma[aR][bR];
    ma[aR][bR]=k;
	checker(ma);
	//�ߤlĹ�y����A�ߤl��J 
	if(ma[1][0]=='R'){
		cout<<"���ߨߤl���\\���}�F�y���̡A�ߤl���!"<<endl;
		return 0; 
	}

	//�y����J 
	cout<<"�п�J�n���ʪ��y�����ɪ��y��:";
	
	do{
	    cin>>cD>>dD;
		k=0;
		//���b:��J����l�y�Ф������n���y�� 
		while(ma[cD][dD]!='D'){
			cout<<"�ݨӧA�a���������b�o�̡A�֥h���a!"<<endl;
	    	cout<<"�Э��s��J�n���ʪ��y�����ɪ��y��:";
	    	continue;
	    	k=1;	
		}
	}while(k==1);
	cout<<"�Ъ��a��J�y���n�e�����y��:";
	
	do{ cin>>aD>>bD;
		k=0;
    	//���b:�P�_�i���i�H��J�y�� 
	    if((aD==0&&(bD>3||bD<1))||(aD==1&&(bD<0||bD>4))||(aD==2&&(bD>3||bD<1))||(aD>=3)){
	    	cout<<"�z���y�����i�¬}�̰�!"<<endl;
	    	cout<<"�Э��s��J���e�����y��:";
	    	k=1;
			continue;
	    }
	    //���ਫ�W�L�@��
		if(((aD!=cD)&&(aD!=(cD+1))&&(aD!=(cD-1)))||((bD!=dD)&&(bD!=(dD+1))&&(bD!=(dD-1)))){
			cout<<"�@���u�ਫ�@���!"<<endl;
			cout<<"�Э��s��J���e�����y��:";
			k=1; 
    		continue;
    		
		}
	    //�������q 
		if((((cD==1&&dD==1)||(cD==1&&dD==3))&&(aD==0||aD==2)&&bD==2)||(((cD==0&&dD==2)||(cD==2&&dD==2))&&(aD==1||aD==3)&&aD==1)){
			cout<<"�������q!"<<endl;
			cout<<"�Э��s��J���e�����y��:";
			k=1;
    		continue;
    	
		}
		//���b:���੹�^��
		if(bD<dD){
			cout<<"�Ӯ��y���O���|���^�Y����!"<<endl;
			cout<<"�Э��s��J���e�����y��:";
			k=1;
    		continue;
    	
		} 
		//���b:����ݦb�������
		if(ma[aD][bD]=='D'){
			if(aD==cD&&bD==dD){
			    cout<<"���௸�b��a���ʳ�!"<<endl;
	        	cout<<"�Э��s��J���e�����y��:";
	        	k=1;
	        	continue;
	       		
			}
			else{
			cout<<"�y���̦b�P�@�Ӧ�m�i�O�|���[��!"<<endl;
			cout<<"�Э��s��J���e�����y��:";
			k=1;
    		continue;
			}
		}
    	//���b:�P�_�o�@��O���O�ߤl 
    	if(ma[aD][bD]=='R'){
    		cout<<"�ߤl��F�A���y���@�}�A��A��^�F��Ӫ���m�A�֥h�_���a!"<<endl; 
    		cout<<"�Э��s��J���e�����y��:";
    		k=1;
    		continue;
    	}
	
    }while(k==1);
	k=ma[cD][dD];
    ma[cD][dD]=ma[aD][bD];
    ma[aD][bD]=k;
	checker(ma);
	//�y��Ĺ�ߤl��A�y����J 
	//0,2
	if(ma[0][2]=='R'&&(ma[0][1]==ma[1][2]&&ma[1][2]==ma[0][3]&&ma[1][2]=='D')){
	    cout<<"�����y���̮���F�ߤl�A�y�����!"<<endl;
		return 0;	
	} 
	//2,2
	else if(ma[2][2]=='R'&&(ma[2][1]==ma[1][2]&&ma[1][2]==ma[2][3]&&ma[1][2]=='D')){
	    cout<<"�����y���̮���F�ߤl�A�y�����!"<<endl;
		return 0;	
	}
	//1,4
	else if(ma[1][4]=='R'&&(ma[0][3]==ma[1][3]&&ma[1][3]==ma[2][3]&&ma[1][3]=='D')){
	    cout<<"�����y���̮���F�ߤl�A�y�����!"<<endl;
		return 0;	
	}
    } 
} 
