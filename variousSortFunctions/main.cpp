#include "InsertionSorter.cpp"
#include "QuickSorter.cpp"
#include "HeapSorter.cpp"
#include "timer.h"

using namespace std;

int main()
{
	Timer t;
	double eTime;
	
	InsertionSorter iS(45293);
	QuickSorter qS(45293);
	HeapSorter hS(45293);
	
	iS.insertAllFromFile(10, "random.txt");
	qS.insertAllFromFile(10, "random.txt");
	hS.insertAllFromFile(10, "random.txt");
	
	t.start();
	for (int i = 1; i <= 10; ++i)
	{
		t.start();
		iS.sort(i);
		t.elapsedUserTime(eTime);
		cout << "File: Random.txt. Partition: " << i << "/10. Function: insertionSort. Time: " << eTime << endl;
		t.start();
		qS.sort(i);
                t.elapsedUserTime(eTime);
                cout << "File: Random.txt. Partition: " << i << "/10. Function: quickSort. Time: " << eTime << endl;
		t.start();
		hS.sort(i);
		t.elapsedUserTime(eTime);
		cout << "File: Random.txt. Partition: " << i << "/10. Function: heapSort. Time: " << eTime << endl;
	}	
		
	return 1;
}
