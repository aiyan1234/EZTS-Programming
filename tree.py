class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def preorder(self,root):
        if root==None:
            return
        else:
            print(root.data,end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self,root):
        if root==None:
            return
        else:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)
    def postorder(self,root):
        if root==None:
            return
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=' ')
    '''def bfs(self,root):
        if root is None:
            return
        q=[]
        q.append(root)
        while q:
            value=q.pop(0)
            print(value.data,end=' ')
            if value.left:
                q.append(value.left)
            if value.right:
                q.append(value.right)'''
        
    def bfs(self,root):
            q=[root]
            q.append(None)
            while q:
                curr=q.pop(0)
                if curr==None:
                    if len(q)==0:
                        return
                    else:
                        print()
                        q.append(None)
                else:
                    print(curr.data,end=" ")
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
    def height(self,root):
        if root==None:
            return 0
        lh=self.height(root.left)
        rh=self.height(root.right)
        return (max(lh,rh)+1)
    def leaves(self,root):
        if root==None:
            return 0
        lh=self.leaves(root.left)
        rh=self.leaves(root.right)
        if lh==0 and rh==0:
            print(root.data)
   
            







if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    root.left.left.left=Node(8)
    root.left.left.right=Node(9)
    print("Preorder traversal:")
    root.preorder(root)
    print("\nInorder traversal:")
    root.inorder(root)
    print("\nPostorder traversal:")
    root.postorder(root)
    print("\nbfs")
    root.bfs(root)

    print("\n height")
    print(root.height(root))
    print("\n leaves")
    root.leaves(root)


