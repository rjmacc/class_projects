#include <string>
#include <iostream>

using namespace std;

class Edge
{
public:
	int src;
	int dst;
	int weight;

	Edge(int s, int d, int w)
		:src{s}, dst(d), weight(w) {}

	Edge reverse()
	{
		return Edge(dst, src, weight);
	}

	void print(ostream & out)
	{
		out << "SRC: " << src << " DST: " << dst << " Weight: " << weight << endl;
	}
};
