#include "Edge.cpp"
#include <vector>

using namespace std;

class Vertex
{
public:
	int id;
	vector<Edge> edges;	

	int num_edges = 0;

	Vertex(int i = 69)
		:id(i) {}

	void add_edge(const Edge & e)
	{
		if (e.src == id)
		{
			edges.push_back(e);
			num_edges++;
		}
	}

	void print(ostream & out)
	{
		out << "Vector id: " << id << "  List of edges:" << endl;
		for (int i = 0; i < num_edges; ++i)
		{
			edges.at(i).print(out);
		}	
	}
};
