#include <stdio.h> 
#include <stdlib.h>

typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node;

int get_height(node* root) {
    return root ? root->ht : -1;
}

void set_height(node* p) {
    int height_left = get_height(p->left);
    int height_right = get_height(p->right);
    p->ht = max(height_left, height_right) + 1;
}

int get_balance(node* root) {
    int l_b = get_height(root->left);
    int r_b = get_height(root->right);
    
    return l_b - r_b;
}

node* rotate_right(node* p) {
    node* q = p->left;
    
    p->left = q->right;
    q->right = p;
    
    set_height(p);
    set_height(q);

    return q;
}

node* rotate_left(node* q) {
    
    node*p = q->right;
    q->right = p->left;
    p->left = q;
    
    set_height(q);
    set_height(p);

    return p;

}

node * rebalance(node* root) {
    set_height(root);
    
    if( get_balance(root)==-2 )
    {
        if( get_balance(root->right) > 0 )
            root->right = rotate_right(root->right);
        return rotate_left(root);
    }
     
    if( get_balance(root)==2 )
    {
        if( get_balance(root->left) < 0  )
            root->left = rotate_left(root->left);
        return rotate_right(root);
    }
    
    return root;
}

node * insert(node * root,int val) {
    if (!root) {
        root = (node *) malloc(sizeof(node));
        root->val = val;
        root->left = NULL;
        root->right = NULL;
        root->ht = 0;
        
        return root;
    }
    
    if (root->val > val)
         root->left = insert(root->left, val);
    else if (root->val < val)
        root->right = insert(root->right, val);
    
    return rebalance(root);
}
