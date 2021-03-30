#include "Sorter.cpp"

using namespace std;

class InsertionSorter : public Sorter
{
public:
	InsertionSorter(int max_capacity)
		:Sorter(max_capacity)  {}
		
	void sort(int partition)
	{
		for (int i = 1; i <= partition * capacity / 10; ++i)
		{
			for (int j = 0; j <= partition * capacity / 10; ++j)
			{
				if (A[i] < A[j])
				{
					swap(A[i], A[j]);
				}
			}
		}	
	}
	
	
};
