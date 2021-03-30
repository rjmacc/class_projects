#include "Graph.cpp"

using namespace std;

class PriorityQueue
{
public:

	struct QueueNode(Vertex v)
	{
		int id = v.id;
	}


	QueueNode *A;
	int capacity;	
	int rear = 0;
	int front = 0;

	PriorityQueue(int cap)
		:A{new QueueNode[cap]}, capacity{cap} {}


	void enqueue(Vertex v)
	{
		QueueNode q = new QueueNode(v);
		A[rear] = q;
		rear = rear + 1 % capacity;
		sort();	
	}

	int dequeue()
	{
		QueueNode q = A[0];
		front = (front + 1) % capacity;;
		return q.id;
	}
	
	int peek()
	{
		return A[curr_size].id;
	}

	~PriorityQueue()
	{
		delete[] A;
	}
	
	bool isEmpty()
	{
		return (front == rear);
	}

private:
	void sort()
	{
		for (int start = rear/2-1; start  >= front; start--)
		{
			siftSmallestDown(start, curr_size);
		}
		for (int end = rear - 1; end > start; end--)
		{
			swap(A[0], A[end]);
			siftSmallestDown(0, end);
		}

	}

	void siftSmallestDown(int start, int end)
	{
		int i = end;
		int left = 2*end+1;
		int right = 2*end+2;

		if (left < start && A[left].weight > A[i].weight)
		{
			i = left;
		}
		
		if (right < start && A[right].weight > A[i].weight)
		{
			i = right;
		}
		
		if (i != end)
		{
			swap(A[end], A[i]);
			siftSmallestDown(start, i);		
		}
	}
}; 


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

