#include <iostream>
#include <string>
#include <fstream>
#include "timer.h"
#include "BinarySearchTree.cpp"

using namespace std;

void insertAllWords(BinarySearchTree<string, int> T, int partition, string fileName)
{
        Timer t;
        double eTime;
        t.start();
        ifstream in(fileName);
        string temp;
        int counter;
        int max = partition * 4529;
        while (in >> temp)
        {
                counter++;
                T.insert(temp, 1);
                if (counter >= max)
                {
                        break;
                }
        }
        in.close();
        t.elapsedUserTime(eTime);
        cout << "File: " << fileName << ". Partition: " << partition << "/10. Function: insertAllWords. Time: " <<  eTime << endl;
}


void findAllWords(BinarySearchTree<string, int> T, int partition, string fileName)
{
        Timer t;
        double eTime;
        t.start();
        ifstream in(fileName);
        string temp;
        int counter;
        int max = partition * 4529;
        while (in >> temp)
        {
                counter++;
                int ph = T.find(temp);
                if (counter >= max)
                {
                        break;
                }
        }
        in.close();
        t.elapsedUserTime(eTime);
        cout << "File: " << fileName << ". Partition: " << partition << "/10. Function: findAllWords. Time: " <<  eTime << endl;
}

void removeAllWords(BinarySearchTree<string, int>  T, int partition, string fileName)
{
        Timer t;
        double eTime;
        t.start();
        ifstream in(fileName);
        string temp;
        int counter;
        int max = partition * 4529;
        while (in >> temp)
        {
                counter++;
                T.find(temp);
                if (counter >= max)
                {
                        break;
                }
        }
        in.close();
        t.elapsedUserTime(eTime);
        cout << "File: " << fileName << ". Partition: " << partition << "/10. Function: removeAllWords. Time: " <<  eTime << endl;
}


void measureAll(string fileName)
{
        for (int i = 1; i <= 10; ++i)
        {
                BinarySearchTree<string, int> T;
                insertAllWords(T, i, fileName);
                findAllWords(T, i, fileName);
                removeAllWords(T, i, fileName);
        }
}

int main()
{
        measureAll("random.txt");
        return 0;
}

