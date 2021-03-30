#include "PriorityQueue.cpp"

using namespace std;

//O(NlogN)
//Does not work because I cannot correctly find each vertex weight
void dijkstras(Graph g, Vertex s, int dist[], int prev[])
{
	PriorityQueue Q(g.capacity);
	for (int i = 0; i < g.capacity; ++i)
	{
		dist[g.vertices[i].id] = 45293;
		prev[g.vertices[i].id] = -1;
		Q.enqueue(g.vertices[i]);
	}
	dist[s.id] = 0;
	int counter = 0;
	while (!Q.isEmpty())
	{
		int id = Q.dequeue();
		Vertex u = g.vertices[id];
		for (int i = 0; i < g.vertices[counter].num_edges; ++i)
		{
			Vertex v = g.vertices[counter].edges[i].dst;
			if (dist[v.id] > dist[u.id] + g.vertices[counter].edges[i].weight)
			{
				dist[v.id] = dist[u.id] + g.vertices[counter].edges[i].weight;
				prev[v.id] = u.id;	
			}
		}
		counter++;
	}
}
