#include <fstream>
#include <string>
#include <iostream>

using namespace std;

class Sorter
{
public:

	string *A;	
	int capacity;
	int curr_size = 0;	

	Sorter(int max_capacity)
		:A{new string[max_capacity]}, capacity{max_capacity}
	{}
	
	void insertAllFromFile(int partition, string fileName)
	{
		string temp;
		ifstream in(fileName);
		while (in >> temp)
		{
			A[curr_size] = temp;
			curr_size++;
			if (curr_size >= partition * capacity / 10)
			{
				break;
			}	
		}
		in.close();
	}
	
	void print(ostream & out)
	{
		for (int i = 0; i < capacity; i++)
		{
			out << A[i] << endl;
		}
	}

	virtual void sort(int partition) = 0;

	~Sorter()
	{
		delete[] A;
	}
};	

