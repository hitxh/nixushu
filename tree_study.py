
class BTree:
    def __init__(self,value):
        self.left =None
        self.data = value
        self.right =None
    def insertLeft(self,value):
        self.left =BTree(value)
        return self.left
    def insertRight(self,value):
        self.right =BTree(value)
        return self.right
    def show(self):
        print(self.data)
#中序遍历 先遍历左子树
def inorder(node):
    if node.data:
        if node.left:               # 有左子叶  继续递归调用
            inorder(node.left)
            node.show()
        elif not node.left:         # 没有左子叶 输出当前数据
           node.show()
        if node.right:               #
            inorder(node.right)

    #中序遍历，先遍历右子树
def rinorder(node):
    if node.data:
        if node.right:
            rinorder(node.right)
            node.show()
        elif not node.right:
            node.show()
        if node.left:
            rinorder(node.left)
def insert(node,value):
    if value > node.data:
        if node.right:
            insert(node.right,value)
        else:
             node.insertRight(value)
    else:
        if node.left:
           insert(node.left,value)
        else:
           node.insertLeft(value)
if __name__ =='__main__':
    l =[3,5,7,20,43,2,15,30]
    Root=BTree(l[0])
    node =Root
    for i in range(1,len(l)):
        insert(Root,l[i])
    print('***********************')
    print('从小到大')
    print('***********************')
    inorder(Root)
    print('***********************')
    print('从大到小')
    print('***********************')
    rinorder(Root)
    print('***********************')