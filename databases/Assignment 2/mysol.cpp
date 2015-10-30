/*

Implementing a B+ Tree in C++

*/

#include <fstream>
// #include<conio>
#include <iomanip>
#include <stdio.h>
#include <time.h>
#include <string>
#include <iostream>
#include <stdlib.h>
#include <algorithm>

using namespace std;
// using std::to_string;

int max_keys;
int count_total=1;
string root="0.txt";
string format=".txt";
string temp_child_1,temp_child_2;

void set_maxkey_value(string filename)
{
    ifstream myfile (filename.c_str());
    if (myfile.is_open())
    {
        // while (myfile.good())
        // {
        	myfile >> max_keys;
        // }
        myfile.close();
    }
    else 
    {  
        //cout << "Unable to open file "<<filename<<endl; 
    }
    //cout<<"Setting the maxkeys to "<<max_keys<<endl;
}	

void intialize_root()
{
	string filename=root;
	ofstream myfile (filename.c_str());
	int number_of_elements=0;
	count_total=1;
	bool isleaf = true;
    if (myfile.is_open())
    {
        myfile << number_of_elements;
        myfile << " ";
        myfile << isleaf;
        myfile << "\n";
        myfile.close();
    }
    else 
    {  
        //cout << "Unable to open file "<<filename<<endl; 
    }
}


float split(string filename, float* allkeys, string allkeys_value[], bool isleaf)
{
	//cout<<"Split : filename: "<<filename<<"....isleaf:"<<isleaf<<endl;
	string temp;
	char Result[50];
	sprintf ( Result, "%d", count_total );
	temp_child_1= filename;
	temp_child_2= Result+format;
	count_total++;
	ofstream myfile1 (temp_child_1.c_str());
	ofstream myfile2 (temp_child_2.c_str());
	int element_count= (max_keys+1)/2;
	//cout<<"Tempo file: "<<temp_child_1<<temp_child_2<<endl;
	if(isleaf)
	{
		myfile2 << " "<<max_keys + 1 - element_count<<" 1\n";
		myfile1 << " "<<element_count<<" 1\n";
		for (int i = 0; i < element_count; ++i)
		{
			myfile1 <<" "<< allkeys[i] << " " << allkeys_value[i]<<" ";
		}
		for (int i = element_count; i <= max_keys; ++i)
		{
			myfile2 <<" "<< allkeys[i] << " " << allkeys_value[i]<<" ";
		}
	}
	else
	{
		element_count= max_keys/2;
		myfile1 << " "<<element_count << " 0\n";
		myfile2 <<" "<< max_keys - element_count << " 0\n";
		for (int i = 0; i < element_count; ++i)
		{
			myfile1 << " "<< allkeys_value[i]<< " "<< allkeys[i]<<" ";
		}
		myfile1 <<" "<< allkeys_value[element_count]<<" ";
		for (int i = element_count+1; i <= max_keys; ++i)
		{
			myfile2 <<" "<< allkeys_value[i]<< " "<< allkeys[i]<<" ";
		}
		myfile2 <<" "<< allkeys_value[max_keys+1]<<" ";
	}
	myfile1.close();
	myfile2.close();


	return allkeys[element_count];
}

float insert_key(float key, string key_value, string filename)
{
	//cout<<"Insertion : Key: "<<key<<"\tValue: "<<key_value<<"\tFilename: "<<filename<<endl;
	int number_of_elements;
	bool isleaf;
	float t_key;
	string t_key_value,t_file; 
	ifstream myfile (filename.c_str());
    if (myfile.is_open())
    {
        // while (myfile.good())
        // {
        	myfile >> number_of_elements >> isleaf
;    		// float allkeys[number_of_elements+1];
    		// string allkeys_value[number_of_elements+1];
        	if(isleaf)
        	{
        		// //cout<<"entered isleaf";
        		//cout<<"Isleaf function\n";
        		float allkeys[max_keys+4];
    			string allkeys_value[max_keys+4];
        		bool check = false;
        		for (int i = 0; i < number_of_elements; ++i)
        		{
        			// myfile >> allkeys[i] >> allkeys_value[i];
        			myfile >> t_key >> t_key_value;
        			if(key < allkeys[i])
        			{
        				allkeys[i+1] = t_key;
        				allkeys_value[i+1] = t_key_value;
        				if(!check)
        				{
        					allkeys[i]=key;
        					allkeys_value[i]=key_value;
        					check = true;
        				}
        			}
        			else
        			{
        				allkeys[i]=t_key;
        				allkeys_value[i]=t_key_value;
        			}
        		}
        		if(!check)
        		{
        			allkeys[number_of_elements]=key;
					allkeys_value[number_of_elements]=key_value;
					// check = true;
        		}
        		else
        		{
        			myfile >> allkeys[number_of_elements] >> allkeys_value[number_of_elements];
        		}
        		myfile.close();
        		
        		if(number_of_elements == max_keys)
        		{
        			//cout<<"It is a leaf , calling split from insert\n";
        			for (int k = 0; k < number_of_elements; ++k)
        			{
        				//cout<<"allkeys["<<k<<"] == "<<allkeys[k]<<"....allkeys_value["<<k<<"]=="<<allkeys_value[k]<<endl;
        			}
        			float x= split(filename, allkeys, allkeys_value, isleaf);
        			// //cout<<"\nhi\n";
        			return x;
        		}
        		else
        		{
        			ofstream file (filename.c_str());
				    if (file.is_open())
				    {
				    	file <<" "<< number_of_elements + 1 << " 1\n";
				    	for (int i = 0; i < number_of_elements+1; ++i)
				    	{
				    		file <<" "<< allkeys[i]<<" "<<allkeys_value[i]<<" ";
				    	}
				    }
				    file.close();
				    return -1;
        		}
        		//cout<<"exited is leaf function \n\n";



        	}
        	else
        	{
        		//cout<<"Not a leaf \n";
        		float allkeys[max_keys+4];
    			string file_array[max_keys+4];
    			int i,j=0;
        		for (i = 0,j=0; i < number_of_elements; ++i,++j)
        		{
        			myfile >> file_array[j] >> allkeys[j];
        			if(key < allkeys[j])
        			{
        				break;
        			}
        		}
				if(i!= number_of_elements)
				{
					//cout << "i == number of elemests ....calling insert with key ,key_value and file_array"<<key<<key_value<<file_array[j]<<endl;
					float return_value= insert_key(key, key_value, file_array[j]);
					if(return_value != -1)
					{
						allkeys[j+1]= allkeys[j];
						allkeys[j]= return_value;
						file_array[j+1]=temp_child_2;
						file_array[j]=temp_child_1;
						for (j=j+2,i++; i < number_of_elements; ++i,++j)
						{
							myfile >> file_array[j] >> allkeys[j];
						}
						myfile >> file_array[j];
						myfile.close();
					}
					else
					{
						myfile.close();
						return -1;
					}
				}
				else
				{
					myfile>> file_array[j];
					////cout << "calling insert with key ,key_value and file_array in is leaf \t"<<key<<key_value<<file_array[j]<<endl;
					float return_value = insert_key(key, key_value, file_array[j]);
					if(return_value == -1)
					{
						myfile.close();
						return -1;
					}
					else
					{
						////cout<<"\nhi\nj=="<<j<<temp_child_2<<endl;
						file_array[j+1]= temp_child_2;
						////cout<<"\nhi\n";
						file_array[j] = temp_child_1;
						allkeys[j] = return_value;
						myfile.close();
						// ////cout<<"\nhi\n";
					}
				}
				if(number_of_elements == max_keys)
				{
					////cout<<"Not a leaf , calling split from insert\n";
					float x= split(filename,allkeys,file_array,isleaf);
					return x;
				}
				else
				{
					ofstream file (filename.c_str());
					////cout<<"check";
				    // if (file.is_open())
				    // {
				    	int i;
				    	file << number_of_elements + 1 << " 0\n";
				    	for (i = 0; i < number_of_elements+1; ++i)
				    	{
				    		file << file_array[i]<<" "<<allkeys[i]<<" ";
				    	}
				    	file<<file_array[number_of_elements+1]<<" ";
				    // }
				    file.close();
				    return -1;
				}
				////cout<<"exited non-leaf function \n\n";
				// else
				// {
				// 	return -1;
				// }
        	}
        // }
        // myfile.close();
    }
    else 
    {  
        cout << "Unable to open file "<<filename<<endl; 
    }
}

void range_query(float start, float end, string filename)
{
	//cout<<"Range Query : Start ->"<<start << "\t End: "<<end<<endl;


}

void queries_init(string filename)
{
	int type_of_query;
	float start, end, key;
	string key_value;
	ifstream myfile (filename.c_str());
    if (myfile.is_open())
    {
        while (myfile.good())
        {
			myfile >> type_of_query;
			if(type_of_query == 0)
			{
				myfile >> key;
				// myfile >> "\n";
				myfile >> key_value;
				insert_key(key,key_value,root); 
			}
			else if(type_of_query == 2)
			{
				myfile >> start;
				myfile >> end;
				range_query(start,end,root);
			}
			else
			{
				//IGNORE ANY QUERY OTHER THAN ABOVE 2
			}
			     	
        }
        myfile.close();
    }
    else 
    {  
        cout << "Unable to open file "<<filename<<endl; 
    }
	//cout<<"All the queries have been processed\n";
}

void input_init(string filename)
{
	float key;
	string key_value;
	ifstream myfile (filename.c_str());
    if (myfile.is_open())
    {
        while (myfile.good())
        {
			myfile >> key;
			myfile >> key_value;
			// float return_value=insert_key(key,key_value,root); 
			if(insert_key(key,key_value,root) != -1)
			{
				string temp_child_3;
				char Result[50];
				sprintf ( Result, "%d", count_total );
				temp_child_3=Result+format;
				count_total++;
				ofstream myfile3 (temp_child_3.c_str());
				myfile3 << "1 0\n"<<temp_child_1 << " "<< return_value << " "<< temp_child_2 << " ";
				root=temp_child_3;
			}
        }
        myfile.close();
    }
    else 
    {  
        cout << "Unable to open file "<<filename<<endl; 
    }
	//cout<<"Points from the file "<<filename<< " has been inserted \n";
}

int main()
{
	string input="assgn2_bplus_data.txt",queries="querysample.txt";
	string file_maxkeys="bplustree.config";
	string sample_input="a.txt";
	cout<<"Processing.........\n";
	intialize_root();
	set_maxkey_value(file_maxkeys);
	cout<<"Inserting the points from assgn2_bplus_data.txt\n";
	input_init(input);
	// input_init(sample_input);
	// cout<<"Processing the queries\n";
	// queries_init(queries);
	return 0;
}