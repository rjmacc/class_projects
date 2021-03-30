using namespace std;

class QuickSorter : public Sorter
{
public:
	QuickSorter(int max_capacity)
		:Sorter(max_capacity)	{}

	void sort(int partition)
	{
		int low = 0;
		int high = partition * capacity / 10 - 1;
		quicksort(low, high);
	}

	void quicksort(int low, int high)
	{
		if (high - low < 10)
		{
			for (int i = low + 1; i <=  high - low; ++i)
			{
				for (int j = low; j <= high-low; ++j)
				{
					if (A[i] < A[j])
					{
						swap(A[i], A[j]);
					}
				}
			}
		} else {
			string pivot = median_of_three(low, high);
			int i = partition(low, high, pivot);
			quicksort(low, i-1);
			quicksort(i+1, high);
		}
	}

        string median_of_three(int low, int high)
        {
                int mid = low + (high - low) / 2;
                if (A[mid] < A[low])
                {
                        swap(A[low], A[mid]);
                }
                if (A[high] < A[low])
                {
                        swap(A[low], A[high]);
                }
                if (A[mid] < A[high])
                {
                        swap(A[mid], A[high]);
                }
                return A[high];
        }

        int partition(int low, int high, string pivot)
        {
                int below = low;
                int above = high - 1;
                while (true)
                {
                        while (A[below] < pivot)
                        {
                                ++below;
                        }
                        while (A[above] > pivot)
                        {
                                --above;
                        }
                        if (below < above)
                        {
                                swap(A[below++], A[above--]);
                        } else {
                                break;
                        }
                }
                swap(A[below], A[above]);
                return below;
        }


};
