#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
using namespace std;

int file_cnt = 1, max_elem  = 8;
string root = "node_0.txt";
string fileinit = "node_", fileformat = ".txt", tempfile1= "", tempfile2 = "";

float split(string filename, float* keyarr, string valarr[], bool isleaf ){
	string temp1 = "";
	tempfile1 = filename;
	temp1 = to_string(file_cnt);
	tempfile2 = fileinit + temp1 + fileformat;
	file_cnt++;
	ofstream f1,f2,f3;
	f1.open(tempfile1.c_str(),ofstream::out);
	f2.open(tempfile2.c_str(),ofstream::out);
	int element_count = (max_elem+1)/2;
	if(isleaf){
		f1 << element_count << " 1\n";
		f2 << max_elem + 1 -element_count << " 1\n";
		for(int i=0;i<element_count;i++){
			f1 << keyarr[i] << " " << valarr[i] << " ";
		}
		for(int i=element_count;i <= max_elem;i++){
			f2 << keyarr[i] << " " << valarr[i] << " ";
		}
	}
	else {
		element_count = max_elem/2;
		f1 << element_count << " 0\n";
		f2 << max_elem - element_count << " 0\n";
		for(int i=0;i<element_count;i++){
			f1 << valarr[i] << " " << keyarr[i] << " ";
		}
		f1 << valarr[element_count];
		for(int i=element_count + 1;i <= max_elem;i++){
			f2 << valarr[i] << " " << keyarr[i] << " ";
		}
		f2 << valarr[max_elem+1];
	}
	f1.close();
	f2.close();
	return keyarr[element_count];
}

float insert(float key, string val, string filename){
	int num_elem;
	bool isleaf;
	ifstream fin (filename, ifstream::in);
	fin >> num_elem >> isleaf;
	float temp_key;
	string file;
	if(isleaf){
		float keyarr[num_elem+1];
		string valarr[num_elem+1];
		bool done = false;
		for(int i = 0;i< num_elem ;i++){
			fin >> keyarr[i] >> valarr[i];
			if(keyarr[i] > key && !done){
				keyarr[i+1] = keyarr[i];
				valarr[i+1] = valarr[i];
				keyarr[i] = key;
				valarr[i] = val;
				done=true;
				i++;
			}
		}
		if(done){
			fin >> keyarr[num_elem] >> valarr[num_elem];
		}
		else{
			valarr[num_elem] = val;
			keyarr[num_elem] = key;
		}
		fin.close();
		string temp_val;
		if(num_elem == max_elem){

			float tempppp = split(filename.c_str(),keyarr,valarr,isleaf);
			return tempppp;
		}
		else{
			ofstream f;
			f.open(filename,ofstream::out);
			f << num_elem + 1 << " 1\n";
			for(int i = 0; i < num_elem +1;i++){
				f << keyarr[i] << " " << valarr[i] << " ";
			}
			return -1;
		}
	}
	else {
		float keyarr[max_elem+1];
		string valarr[max_elem+4];
		int i,j=0;
		for(i=0;i<num_elem;i++,j++){	
			fin >> valarr[j] >> keyarr[j];
			if(key < keyarr[j]){
				break;
			}
		}
		if(i!=num_elem){
			float ret = insert(key, val, valarr[j]);
			if(ret != -1){
				valarr[j+1] = tempfile2;
				valarr[j] = tempfile1;
				keyarr[j+1] = keyarr[j];
				keyarr[j] = ret;
				j++,j++,i++;
				for(;i<num_elem;i++,j++){
					fin >> valarr[j] >> keyarr[j];
				}
				fin >> valarr[j];
				fin.close();
			}
			else{
				fin.close();
				return -1;
			}
		}
		else {
			fin >> valarr[j];
			float ret = insert(key, val, valarr[j]);
			
			if(ret != -1){
				valarr[j+1] = tempfile2;
				valarr[j] = tempfile1;
				keyarr[j] = ret;
				fin.close();
			}
			else {
				fin.close();
				return -1;
			}
		}
		if(num_elem == max_elem){
			return split(filename,keyarr,valarr,isleaf);
		}
		else{
			ofstream f;
			f.open(filename,ofstream::out);
			f << num_elem+1 << " 0\n";
			for(int z=0;z<=num_elem;z++){
				f << valarr[z] << " " <<keyarr[z] << " ";
			}
			f<<valarr[num_elem + 1];
			f.close();
			return -1;
		}
	}

}
bool input(string filename){
	int type;
	float key;
	ifstream fin ;
	fin.open(filename.c_str(), ifstream::in);
	string val;
	for(int i=0;i<30;i++){
		
			
			fin >> key;
			fin >> val;
			float ret = insert(key, val, root);
			if(ret != -1){
				string tempfile3, temp1;
				temp1 = to_string(file_cnt);
				tempfile3 = fileinit + temp1 + fileformat;
				file_cnt++;
				ofstream f;
				f.open(tempfile3.c_str(), ofstream::out);
				f << "1 0\n";
				f << tempfile1 << " " << ret << " " << tempfile2;
				f.close();
				root = tempfile3;
			}

		
	}
}
int main(){
	string s;
	cin >> s;
	input(s);
	cout << root;
	return 0;
}