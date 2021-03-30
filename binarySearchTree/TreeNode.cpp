#include <iostream>
#include <string>

using namespace std;

template <typename KeyType, typename ElementType>

class TreeNode
{
public:

	TreeNode *parent;
        KeyType key;
        ElementType info;
        TreeNode *left;
        TreeNode *right;
	int color = 1; //colors Red/Black. 0 correlates to black and 1 correlates to 1

        TreeNode(KeyType k, ElementType e, TreeNode *l, TreeNode *r, TreeNode *p) :key(k), info(e), left(l), right(r), parent(p)
        {}

        static TreeNode *newNode(KeyType k, ElementType e, TreeNode *l, TreeNode *r, TreeNode *p)
        {
                return new TreeNode(k, e, l, r, p);
        }

	static TreeNode *getParent(TreeNode *node)
	{
		return node->parent;
	}

	static TreeNode *getSibling(TreeNode *node)
	{
		TreeNode *parent = getParent(node);
		if (parent != nullptr)
		{
			if (node == parent->left)
			{
				return parent->right;
			} else {
				return parent->left;
			}
		} else {
			return nullptr;
		}
	}

	static TreeNode *getGrandparent(TreeNode *node)
	{
		TreeNode *parent = getParent(node);
		if (parent != nullptr)
		{
			return parent->parent;
		} else {
			return nullptr;
		}
	}

	static TreeNode *getUncle(TreeNode *node)
	{
		TreeNode *parent = getParent(node);
		TreeNode *gparent = getParent(node);
		if (gparent != nullptr) 
		{
			return nullptr; 
		} else {
			return getSibling(parent);
		}
	}
	
	void rotateLeft(TreeNode *node)
	{
		TreeNode *temp = node->right;
		TreeNode *parent = getParent(node);
		
		if (temp->left != nullptr and temp->right != nullptr)
		{
			node->right = temp->left;
			temp->left = node;
			node->parent = temp;

			if (node->right != nullptr)
			{
				node->right->parent = node;
			}
			
			if (parent != nullptr)
			{
				if (node == parent->left)
				{
					parent->left = temp;
				}
				
				if (node == parent->right)
				{
					parent->right = temp;
				}
			}
			temp->parent = parent;
		}
	}

	void rotateRight(TreeNode *node)
	{
		TreeNode *temp = node->right;
                TreeNode *parent = getParent(node);

                if (temp->left != nullptr and temp->right != nullptr)
                {
                        node->left = temp->right;
                        temp->right = node;
                        node->parent = temp;

                        if (node->left != nullptr)
                        {
                                node->left->parent = node;
                        }

                        if (parent != nullptr)
                        {
                                if (node == parent->left)
                                {
                                        parent->left = temp;
                                }

                                if (node == parent->right)
                                {
                                        parent->right = temp;
                                }
                        }
                        temp->parent = parent;
                }
	
	}

        static TreeNode *insert(KeyType key, ElementType info, TreeNode *root, TreeNode *prev)
        {
                if (root == nullptr)
                {
                        return newNode(key, info, nullptr, nullptr, prev);
                }
                if (key < root->key)
                {
                        root->left  = insert(key, info, root->left, root);
                } else if (key > root->key)
                {
                        root->right = insert(key, info, root->right, root);
                } else {
                        root->info++;
                }
                return root;
        }

	

	void insertRepair(TreeNode *node)
	{
		if (node->parent == nullptr)
		{
			if (getGrandparent(node) == nullptr)
			{
				node->color = 0;
			}
		} else if (node->parent->color == 0) {
		} else if (getUncle(node) != nullptr and getUncle(node)->color== 1) {
			node->parent->color = 0;
			TreeNode *temp = getUncle(node);
			temp->color = 0;
			temp = getGrandparent(node);
			temp->color = 1;
			insertRepair(node);
		} else {
			TreeNode *parent = getParent(node);
			TreeNode *gparent = getGrandparent(node);

			if (node == parent->right and parent == gparent->left)
			{
				rotateLeft(parent);
				node = node->left;
			} else if (node == parent->left and parent == gparent->right)	{
				rotateRight(parent);
				node = node->right;
			}
			
			parent = getParent(node);
			gparent = getGrandparent(node);

			if (node == parent->left)
			{
				rotateRight(gparent);
			} else {
				rotateLeft(gparent);
			}
			parent->color = 0;
			gparent->color = 1;	
		}
	}

        static TreeNode *find(KeyType key, TreeNode *t)
        {
                if (t == nullptr or key == t->key)
                {
                        return t;
                }
                if (key < t->key)
                {
                        return find(key, t->left);
                } else if (key > t->key) {
                        return find(key, t->right);
                }
                return nullptr;
        }

	static TreeNode *remove(KeyType key, TreeNode *t)
        {
                TreeNode *toRemove = find(key, t);
                if (key < t->key)
                {
                        t->left = remove(key, t->left);
                } else if (key > t->key) {
                        t->right = remove(key, t->right);
                } else {
                        if(t->left == nullptr && t -> right == nullptr)
                        {
                                delete t;
                                t = nullptr;
                                return t;
                        } else if(t->left == nullptr) {
                                t = t->right;
                                return t;
                        } else if(t->right == nullptr) {
                                t = t->left;
                                return t;
                        } else {
                                TreeNode *temp = t->right;
                                while (temp->left != nullptr)
                                {
                                        temp = temp->left;
                                }
                                t->info = temp->info;
                                t->key = temp->key;
                                t->right = remove(temp->key, t->right);
                        }
                }
                return t;
        }

static void print(ostream & out, TreeNode * t)
        {
                if (t)
                {
                        out << "[";
                        print(out, t->left);
                        out << "(" << t->key << "," << t->info << ")";
                        print(out, t->right);
                        out << "]";
                } else
                        out << "nullptr";
        }

        static void deleteNode(TreeNode *t)
        {
                delete t;
        }

        static void deleteTree(TreeNode *t)
        {
                if (t)
                {
                        deleteTree(t->left);
                        deleteTree(t->right);
                        deleteNode(t);
                }
        }
};

