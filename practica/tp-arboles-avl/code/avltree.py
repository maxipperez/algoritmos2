import binarytree

class AVLTree:
	root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
	bf = None


# rotateLeft(Tree,avlnode) 
# Descripción: Implementa la operación rotación a la izquierda 
# Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  izquierda
# Salida: retorna la nueva raíz

def rotateLeft(Tree,avlnode):
    # Paso 1: 
    if avlnode.rightnode == None: 
        return None 
    
    newRoot = avlnode.rightnode 

    # Paso 3: 
    avlnode.rightnode = newRoot.leftnode
    if newRoot.leftnode != None: 
        newRoot.leftnode.parent = avlnode

    newRoot.parent = avlnode.parent 
    if avlnode.parent == None: 
        Tree.root = newRoot 
    else: 
        if avlnode.parent.rightnode == avlnode: 
            avlnode.parent.rightnode = newRoot
        else: 
            avlnode.parent.leftnode = newRoot 

    # Paso 2:
    newRoot.leftnode = avlnode
    avlnode.parent = newRoot 
    return newRoot 

# rotateRight(Tree,avlnode) 
# Descripción: Implementa la operación rotación a la derecha 
# Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  derecha
# Salida: retorna la nueva raíz

def rotateRight(Tree,avlnode): 

    # Paso 1: 
    if avlnode.leftnode == None: 
        return None 
    
    newRoot = avlnode.leftnode 

    # Paso 3: 
    if newRoot.rightnode != None: 
        newRoot.rightnode.parent = avlnode
        avlnode.leftnode = newRoot.rightnode

    newRoot.parent = avlnode.parent 
    if avlnode.parent == None: 
        Tree.root = newRoot 
    else: 
        if avlnode.parent.rightnode == avlnode: 
            avlnode.parent.rightnode = newRoot
        else: 
            avlnode.parent.leftnode = newRoot 

    # Paso 2:
    newRoot.rightnode = avlnode
    avlnode.parent = newRoot 
    return newRoot 

# calculateBalance(AVLTree) 
# Descripción: Calcula el factor de balanceo de un árbol binario de búsqueda. 
# Entrada: El árbol AVL  sobre el cual se quiere operar.
# Salida: El árbol AVL con el valor de balanceFactor para cada subarbol

def calculateBalance(AVLTree): 

    if AVLTree.root == None: 
        return None 
    else: 
        return calculateBalanceR(AVLTree.root)

def calculateBalanceR(node):

    if node == None: 
        return None
    
    if node.leftnode == None: 
        alturaIzq = -1
    else: 
        alturaIzq = alturaR(node.leftnode)

    if node.rightnode == None: 
        alturaDer = -1
    else: 
        alturaDer = alturaR(node.rightnode)

    node.bf = alturaIzq - alturaDer

    calculateBalanceR(node.leftnode)
    calculateBalanceR(node.rightnode)

    return node

def alturaR(node): 

    if node == None: 
        return -1

    if node.leftnode == None and node.rightnode == None: 
        return 0 
    
    alturaIzq = alturaR(node.leftnode)
    alturaDer = alturaR(node.rightnode)

    return 1 + max(alturaIzq,alturaDer)


# reBalance(AVLTree) 
# Descripción: balancea un árbol binario de búsqueda. Para esto se deberá 
# primero calcular el balanceFactor del árbol y luego en función de esto
# aplicar la estrategia de rotación que corresponda.
# Entrada: El árbol binario de tipo AVL  sobre el cual se quiere operar.
# Salida: Un árbol binario de búsqueda balanceado. Es decir luego 
# de esta operación se cumple que la altura (h) de su subárbol 
# derecho e izquierdo difieren a lo sumo en una unidad.

def reBalance(AVLTree): 

    if AVLTree.root == None: 
        return None 
    else: 
        reBalanceR(AVLTree.root, AVLTree)
        return AVLTree

def reBalanceR(node, tree): 
    if node == None: 
        return None 
    
    reBalanceR(node.leftnode,tree)
    reBalanceR(node.rightnode,tree)

    calculateBalanceR(node)

    if node.bf == None: 
        return None

    if node.bf <= -2: 
        rotateLeft(tree,node)
    if node.bf >= 2:
        rotateRight(tree,node)






    