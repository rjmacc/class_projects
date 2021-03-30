#include "Graph.cpp" 

using namespace std;

int main()
{
	cout << "-------Testing Vertex constructor-------" << endl;
	Vertex v(1);
	v.print(cout);
	
	cout << "-------Testing Edge constructor-------" << endl;
	Edge coochie(1,3, 10);
	Edge moochie(1,2, 11);
	Edge toochie(3,2, 15);
	coochie.print(cout);
	moochie.print(cout);
	toochie.print(cout);

	cout << "-------Testing Add_Edge-------" << endl;
	v.add_edge(coochie);
	v.add_edge(moochie);
	v.add_edge(toochie);
	v.print(cout);
	
	cout << endl << endl << "-------Testing Graph constructor-------" << endl;
	Graph g("small.graph.txt");
	g.print(cout);
		
	return 1;
}
