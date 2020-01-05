#BST
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data=data


class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return cur

    def levelOrder(self,root):
        quene=[root]
        for current in quene:
            if current:
                print(current.data,end=" ")
                quene.append(current.left)
                quene.append(current.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)




