#include "TreeNode.cpp"
#include <iostream>

template<typename KeyType, typename ElementType>

class BinarySearchTree
{
        TreeNode<KeyType, ElementType> *root = nullptr;

public:	

	void insert(KeyType key, ElementType info)
        {
                root = TreeNode<KeyType, ElementType>::insert(key, info, root, nullptr);
        	
		root->insertRepair(root);
		while (TreeNode<KeyType, ElementType>::getParent(root) != nullptr)
		{
			root = TreeNode<KeyType, ElementType>::getParent(root);
		}
	}

        ElementType find(KeyType key)
        {
                TreeNode<KeyType, ElementType> *temp = TreeNode<KeyType, ElementType>::find(key, root);
                if (!temp)
                {
                        insert(key, 1);
                        temp = TreeNode<KeyType, ElementType>::find(key, root);
                }
                return temp->info;
        }

        void remove(KeyType key)
        {
                TreeNode<KeyType, ElementType>::remove(key, root);
        }

        int operator[] (KeyType key)
        {
                TreeNode<KeyType, ElementType> *temp = TreeNode<KeyType, ElementType>::find(key, root);
                if (!temp)
                {
                        return 0;
                } else {
                        return temp->info;
                }
        }

        void print(ostream & out)
        {
                TreeNode<KeyType, ElementType>::print(out, root);
        }

        ~BinarySearchTree()
        {
                TreeNode<KeyType, ElementType>::deleteTree(root);
        }

};

