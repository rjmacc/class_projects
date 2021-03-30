#include "Vertex.cpp"
#include <fstream>

using namespace std;

class Graph
{
public:
	int capacity;
	Vertex * vertices; 

	Graph(string file_name)
	{
		ifstream in;
		in.open(file_name);
		in >> capacity;
		vertices = new Vertex[capacity];
		for (int i = 0; i < capacity; ++i)
		{
			vertices[i].id = i;
		}
		while (!in.eof())
		{
			int src;
			in >> src;
			int dst;
			in >> dst;
			int weight;
			in >> weight;
			add_edge(src, dst, weight);
		}
		in.close();
	}

	void add_edge(int src, int dst, int w)
	{
		Edge temp = Edge(src, dst, w);
		vertices[src].add_edge(temp);
		vertices[dst].add_edge(temp.reverse());
		
	}
	
	void print(ostream & out)
	{
		for (int i = 0; i < capacity; ++i)
		{
			vertices[i].print(out);
		}
	}

	~Graph()
	{
		delete[] vertices;
	}	
};
