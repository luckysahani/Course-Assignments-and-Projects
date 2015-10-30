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
#include <sys/time.h>
#include <unistd.h>
#include <vector>
#include <math.h>
// #include <chrono>

using namespace std;

int max_keys;
int count_total=1;
string root="0.txt";
string format=".txt";
string temp_child_1,temp_child_2;
string query_output="";
vector <double> vector_insert,vector_range,vector_find;
// string sibling;
// struct timeval {
//   time_t tv_sec;
//   suseconds_t tv_usec;
// };

void set_maxkey_value(string filename)
{
    ifstream myfile (filename.c_str());
    if (myfile.is_open())
    {
        while (myfile.good())
        {
        	myfile >> max_keys;
        }
        myfile.close();
    }
    else 
    {  
        cout << "Unable to open file "<<filename<<endl; 
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
        myfile << " ";
        myfile << "done" <<"\n";
        myfile.close();
    }
    else 
    {  
        cout << "Unable to open file "<<filename<<endl; 
    }
}


float split(string filename, float* allkeys, string allkeys_value[], bool isleaf,string sibling)
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
		myfile2 << " "<<max_keys + 1 - element_count<<" 1 ";
		myfile1 << " "<<element_count<<" 1 ";
		myfile1<<temp_child_2<<"\n";
		// cout<<"Sibling is "<<sibling<<" and "<<temp_child_2<<"\n";
		myfile2<<sibling<<"\n";
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
	string sibling;
	ifstream myfile (filename.c_str());
    if (myfile.is_open())
    {
        // while (myfile.good())
        // {
        	myfile >> number_of_elements >> isleaf;
        	if(isleaf)
			{
        	myfile >> sibling;
        	}        	// float allkeys[number_of_elements+1];
    		// string allkeys_value[number_of_elements+1];
        	if(isleaf)
        	{
        		// //cout<<"entered isleaf";
        		//cout<<"Isleaf function\n";
        		float allkeys[number_of_elements+1];
    			string allkeys_value[number_of_elements+1];
    			
        		bool check = false;
        		for (int i = 0; i < number_of_elements; ++i)
        		{
        			// myfile >> allkeys[i] >> allkeys_value[i];
        			myfile >> allkeys[i] >> allkeys_value[i];
        			if((key < allkeys[i]) && !check)
        			{
        				allkeys[i+1] = allkeys[i];
        				allkeys_value[i+1] = allkeys_value[i];
        				if(!check)
        				{
        					allkeys[i]=key;
        					allkeys_value[i]=key_value;
        					check = true;
        				}
        				i++;
        			}
        			// else
        			// {
        			// 	allkeys[i]=t_key;
        			// 	allkeys_value[i]=t_key_value;
        			// }
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
        			// for (int k = 0; k < number_of_elements; ++k)
        			// {
        			// 	//cout<<"allkeys["<<k<<"] == "<<allkeys[k]<<"....allkeys_value["<<k<<"]=="<<allkeys_value[k]<<endl;
        			// }
        			float x= split(filename, allkeys, allkeys_value, isleaf,sibling);
        			// //cout<<"\nhi\n";
        			return x;
        		}
        		else
        		{
        			ofstream file (filename.c_str());
				    if (file.is_open())
				    {
				    	file << number_of_elements + 1 << " 1 "<<sibling<<endl;
				    	for (int i = 0; i < number_of_elements+1; ++i)
				    	{
				    		file << allkeys[i]<<" "<<allkeys_value[i]<<" ";
				    	}
				    	// file<<sibling<<" ";
				    }
				    file.close();
				    return -1;
        		}
        		//cout<<"exited is leaf function \n\n";



        	}
        	else
        	{
        		//cout<<"Not a leaf \n";
        		float allkeys[max_keys+1];
    			string file_array[max_keys+4];
    			int i,j=0;
        		for (i = 0,j=0; i < number_of_elements; ++i,++j)
        		{
        			myfile >> file_array[j] >> allkeys[j];
        			if(key < allkeys[j])
        			{
        				goto a;
        			}
        		}
				a: if(i!= number_of_elements)
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
					float x= split(filename,allkeys,file_array,isleaf,"");
					return x;
				}
				else
				{
					ofstream file (filename.c_str());
					////cout<<"check";
				    // if (file.is_open())
				    // {
				    	int z;
				    	file << number_of_elements + 1 << " 0\n";
				    	for (z = 0; z < number_of_elements+1; ++z)
				    	{
				    		file << file_array[z]<<" "<<allkeys[z]<<" ";
				    	}
				    	file<<file_array[number_of_elements+1];
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
	bool isleaf;
	int number_of_elements;
	ifstream myfile (filename.c_str());
	string file,key_value,sibling;
	char Result[50];
	float key;
	myfile >> number_of_elements >> isleaf;
	if(start > 1 || end < 0 )
	{
		return;
	}
	if( start < 0){start =0;}
	if( end > 1){end=1;}
	// cout<<"Range Query : Start ->"<<start << "\t End: "<<end<<"\t Isleaf :"<<isleaf<<"\t filename : "<<filename<<endl;
	if(isleaf)
	{
		myfile >> sibling;

		for (int i = 0; i < number_of_elements; ++i)
		{
			myfile>> key >> key_value;
			// cout<<"In Leaf: Start ->"<<start << "\t End: "<<end<<"\t Key :"<<key<<endl;
			if((key >= start)&&(key <=end))
			{
				// cout<<key<<" "<<key_value<<endl;
				
				sprintf ( Result, "%f", key );
				query_output+= Result;
				query_output += "\t" + key_value + "\n";
			}
			if(end < key )
			{
				return;
			}
			// myfile.close();
			
		}
		if(sibling=="done")
		{
			return;
		}
		range_query(key,end,sibling);
	}
	else
	{
		for (int i = 0; i < number_of_elements; ++i)
		{
			myfile>> file >> key;
			// cout<<"In non-leaf: Start ->"<<start << "\t End: "<<end<<"\t Key :"<<key<<endl;
			if(start < key)
			{
				range_query(start,end,file);
				return;
			}
			if(end < key )
			{
				// cout<<"returned\n";
				return;
			}
		}
		myfile>>file;
		myfile.close();
		if(sibling=="done")
		{
			return;
		}
		range_query(start,end,file);
	} 

}
void find_key(float key, string filename)
{
	// cout<<"Find Query : Key = "<<key<<endl;
	range_query(key,key,filename);
}
void queries_init(string filename)
{
	struct timeval start_time, end_time;
	int type_of_query;
	float start, end, key,mid,dev;
	double useconds,mtime,insert_min_time=1000000.0,find_min_time=1000000.0,range_min_time=1000000.0,insert_max_time=0.0,range_max_time=0.0,find_max_time=0.0;
	double range_sum=0.0,range_sum_square=0.0,insert_sum=0.0,insert_sum_square=0.0,find_sum=0.0,find_sum_square=0.0;
	string key_value;

	double range_count=0,insert_count=0,find_count=0;
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
				cout<<"\n Insert Query : Key -> "<<key<<" and Value -> "<<key_value<<endl;
				gettimeofday(&start_time, NULL);
				insert_key(key,key_value,root); 
				gettimeofday(&end_time, NULL);
				useconds = (end_time.tv_usec - start_time.tv_usec)/1000000.0;
				printf("\nElapsed time(microseconds) of Insertion Query: %lf \n", useconds);
				vector_insert.push_back(useconds);
				// if(insert_max_time < useconds)
				// {
				// 	insert_max_time = useconds;
				// }
				// if(insert_min_time > useconds)
				// {
				// 	insert_min_time = useconds;
				// }
				// insert_sum+= useconds;
				// insert_count++;
			}
			else if(type_of_query == 2)
			{
				query_output="";
				myfile >> mid;
				myfile >> dev;
				start=mid-dev;
				end=mid+dev;
				cout<<"Range Query : Start ->"<<start << "\t End: "<<end<<endl;
				gettimeofday(&start_time, NULL);
				range_query(start,end,root);
				gettimeofday(&end_time, NULL);
				useconds = (end_time.tv_usec - start_time.tv_usec)/1000000.0;
				cout<<query_output<<endl;
				vector_range.push_back(useconds);
				printf("Elapsed time(microseconds) of Range Query: %lf \n", useconds);
				// if(range_max_time < useconds)
				// {
				// 	range_max_time = useconds;
				// }
				// if(range_min_time > useconds)
				// {
				// 	range_min_time = useconds;
				// }
				// range_sum+=useconds;
				// range_count++;
			}
			else if (type_of_query == 1)
			{
				query_output="";
				myfile >> key;
				cout<<"\nFind Query : Key = "<<key<<endl;
				gettimeofday(&start_time, NULL);
				find_key(key,root);
				gettimeofday(&end_time, NULL);
				useconds = (end_time.tv_usec - start_time.tv_usec)/1000000.0;
				cout<<query_output<<endl;
				printf("Elapsed time(microseconds) of Point Query: %lf \n", useconds);
				vector_find.push_back(useconds);
				// if(find_max_time < useconds)
				// {
				// 	find_max_time = useconds;
				// }
				// if(find_min_time > useconds)
				// {
				// 	find_min_time = useconds;
				// }
				// find_sum += useconds;
				// find_count++;
			}
			else
			{
				//IGNORE ANY QUERY OTHER THAN ABOVE 2
			}
			     	
        }
        myfile.close();
        double min=100.0,max=0.0,sum=0.0,avg,sum2 = 0.0, avg2;
        for(int i=0; i<vector_find.size();i++){
        	if(vector_find[i] < min) min = vector_find[i];
        	if(vector_find[i] > max) max = vector_find[i];
        	sum+=vector_find[i];
        	sum2+=vector_find[i] * vector_find[i];
        }
        avg = sum/double(vector_find.size());
        avg2 = sum2/double(vector_find.size());
        cout<<"\n\n--------------Find-----------------\n";
        cout<<"Find Minimum Time :"<<min<<endl;
        cout<<"Find Maximum Time :"<<max<<endl;
        cout<<"Find Average Time :"<<avg<<endl;
        cout<<"Standard Deviataion  Time :"<<sqrt(avg2 - avg*avg)<<endl;

        min=100.0,max=0.0,sum=0.0,avg,sum2 = 0.0, avg2;
        for(int i=0; i<vector_insert.size();i++){
        	if(vector_insert[i] < min) min = vector_insert[i];
        	if(vector_insert[i] > max) max = vector_insert[i];
        	sum+=vector_insert[i];
        	sum2+=vector_insert[i] * vector_insert[i];
        }
        avg = sum/double(vector_insert.size());
        avg2 = sum2/double(vector_insert.size());
        cout<<"\n\n--------------Insertion-----------------\n";
        cout<<" Minimum Time :"<<min<<endl;
        cout<<" Maximum Time :"<<max<<endl;
        cout<<" Average Time :"<<avg<<endl;
        cout<<"Standard Deviataion  Time :"<<sqrt(avg2 - avg*avg)<<endl;

        min=100.0,max=0.0,sum=0.0,avg,sum2 = 0.0, avg2;
        for(int i=0; i<vector_range.size();i++){
        	if(vector_range[i] < min) min = vector_range[i];
        	if(vector_range[i] > max) max = vector_range[i];
        	sum+=vector_range[i];
        	sum2+=vector_range[i] * vector_range[i];
        }
        avg = sum/double(vector_range.size());
        avg2 = sum2/double(vector_range.size());
        cout<<"\n\n--------------Range-----------------\n";
        cout<<" Minimum Time :"<<min<<endl;
        cout<<" Maximum Time :"<<max<<endl;
        cout<<" Average Time :"<<avg<<endl;
        cout<<"Standard Deviataion  Time :"<<sqrt(avg2 - avg*avg)<<endl;
    }
    else 
    {  
        cout << "Unable to open file "<<filename<<endl; 
    }
	// cout<<"All the queries have been processed\n";
}

void input_init(string filename)
{
	float key;
	string key_value;
	ifstream myfile (filename.c_str());
	// int i=0;
    if (myfile.is_open())
    {
        while (myfile.good())
        {
        	// if(i>100000){return;}
        	// i++;
			myfile >> key;
			myfile >> key_value;
			float return_value=insert_key(key,key_value,root); 
			if(return_value != -1)
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
	string sample_queries="b.txt";
	cout<<"Processing.........\n";
	intialize_root();
	set_maxkey_value(file_maxkeys);
	cout<<"Inserting the points from assgn2_bplus_data.txt\n";
	input_init(input);
	// input_init(sample_input);
	cout<<"Processing the queries\n";
	queries_init(queries);
	// queries_init(sample_queries);
	return 0;
}