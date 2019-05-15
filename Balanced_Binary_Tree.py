
class Node:
    def __init__(self,d):
        #Инициализация элемента Node
        self.data=d
        self.left=None
        self.right=None

def Get_all_Tree_Wide(Node):
    #Преобразовние массива к бинарному дереву
    treeNode=Node
    levels=0
    if treeNode!=None:
            parents=[]
            children=[]
            output=[]
            output.append(treeNode.data)
            parents.append(treeNode)
            while parents!=[]:
                levels+=1
                #print(levels,"Уровень")
                for everynode in parents:
                        if everynode.left!=False:
                            output.append(everynode.left.data)
                            children.append(everynode.left)
                        else:
                            output.append(None)
                            children.append(None)
                        if everynode.right!=False:
                            output.append(everynode.right.data)
                            children.append(everynode.right)
                        else:
                            output.append(None)
                            children.append(None)
                parents.clear()
                for everynode in children:
                    if everynode!=None:
                        parents.append(everynode)
                    else:
                        pass
                children.clear()
            q_ty=0
            for j in range(0,levels):
                q_ty=q_ty+2**j
            #print(q_ty,"Кол-во")
            output=output[:q_ty]
            return output

def Create_BBSTArray(a,out=[]):
    #Функция преобразования массива к виду бинарного дерева 
    if not a:
        return False
    if out==[]:
        a=Sort_initial_data(a)
    middle=int((len(a))/2)
    out.append(a[middle])
    root=Node(a[middle])
    root.left=Create_BBSTArray(a[:middle],out)
    root.right=Create_BBSTArray(a[middle+1:],out)
    return root

def Sort_initial_data(a,):
    #Сортировка исходного массива
    length=len(a)
    for i in range(0,length):
        for j in range(i,length):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
            else:
                pass
    return a

def Print_Tree(node):
    if not node:
        return
    print(node.data)
    Print_Tree(node.left)
    Print_Tree(node.right)

def GenerateBBSTArray(a):
    #Ф-ция создания бинарного дерева
    BBSTArray=Create_BBSTArray(a)
    Res=Get_all_Tree_Wide(BBSTArray)
    return Res    
"""
a=[299,45,67,78,688,789,66,90,900]
Tree_BT=GenerateBBSTArray(a)
print(Tree_BT)
"""   
