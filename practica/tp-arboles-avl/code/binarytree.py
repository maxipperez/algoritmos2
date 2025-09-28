from algo1 import *

class BinaryTree:
    root=None

class BinaryTreeNode:
    key=None
    value=None
    leftnode=None
    rightnode=None
    parent=None

# search(B,element)
# Descripción: Busca un elemento en el TAD árbol binario.
#     Entrada: el árbol binario B en el cual se quiere realizar la búsqueda 
#     (BinaryTree) y el valor del elemento (element) a buscar.
#     Salida: Devuelve la key asociada a la primera instancia del elemento.
#     Devuelve None si el elemento no se encuentra.
#     if node.value == element:
#         return node.key
#     elif node.leftnode != None:
#         searchLeft = searchR(node.leftnode, element)
    
#     if searchLeft != None:
#         return searchLeft
    
#     return searchR(node.rightnode, element)
def searchR(node, element):

    if node == None:
        return None
    if node.value == element:
        return node.key
    searchleft = searchR(node.leftnode, element)
    if searchleft != None:
        return searchleft

    return searchR(node.rightnode, element)


def search(B, element):
    if B.root != None:
        return searchR(B.root, element)
    else:
        return None
    

# insert(B,element,key)
# Descripción: Inserta un elemento con una clave determinada del TAD
# árbol binario.
# Entrada: el árbol B sobre el cual se quiere realizar la inserción
# (BinaryTree), el valor del elemento (element) a insertar y la clave
# (key) con la que se lo quiere insertar.
# Salida: Si pudo insertar con éxito devuelve la key donde se inserta el
# elemento. En caso contrario devuelve None.


def insertR(currentNode, newNode):
    if currentNode.key != newNode.key:
        if newNode.key > currentNode.key:
            if currentNode.rightnode == None:
                currentNode.rightnode = newNode
                newNode.parent = currentNode
                return newNode.key
            else:
                insertR(currentNode.rightnode, newNode)
        else:
            if currentNode.leftnode == None:
                currentNode.leftnode = newNode
                newNode.parent = currentNode
                return newNode.key
            else:
                insertR(currentNode.leftnode, newNode)

    else:
        return None


def insert(B, element, key):
    newNode = BinaryTreeNode()
    newNode.key = key
    newNode.value = element
    if B.root != None:
        

        return insertR(B.root, newNode)
    else:
        B.root = newNode
    

# delete(B,element)
# Descripción: Elimina un elemento del TAD árbol binario.
# Poscondición: Se debe desvincular el Node a eliminar.
# Entrada: el árbol binario B sobre el cual se quiere realizar la
# eliminación (BinaryTree) y el valor del elemento (element) a eliminar.
# Salida: Devuelve clave (key) del elemento a eliminar. Devuelve None si
# el elemento a eliminar no se encuentra.


def accessNodeR(currentNode, element, key):
    if currentNode != None:
        if currentNode.value != element:
            if key < currentNode.key:
                return accessNodeR(currentNode.leftnode, element, key)
            else:
                return accessNodeR(currentNode.rightnode, element, key)
        else:
            
            return currentNode
    else:
        return None

def accessNode(B, element):
    nodeKey = search(B, element)

    if B.root != None and nodeKey != None:
        
        return accessNodeR(B.root, element, nodeKey)
    else:
        return None

def linkNodes(B, parent, son, nodeToLink):
    if parent != None:

        if parent.leftnode == son:
            parent.leftnode = nodeToLink
        else:
            parent.rightnode = nodeToLink

    else:
        B.root = nodeToLink

def searchHighestLowestNode(nodeToDelete):
    currentNode = nodeToDelete.rightnode

    while currentNode.leftnode != None:
        currentNode = currentNode.leftnode
    
    return currentNode

def delete(B, element):

    nodeToDelete = accessNode(B, element)
    
    if nodeToDelete != None:
        #print(nodeToDelete.value)
        parentNode = nodeToDelete.parent
        
        if nodeToDelete.leftnode == None and nodeToDelete.rightnode == None: #Es una hoja
            nodeToLink = None

        elif nodeToDelete.leftnode != None and nodeToDelete.rightnode == None: #Es una rama con una hoja a la izq
            nodeToLink = nodeToDelete.leftnode
            
        elif nodeToDelete.rightnode != None and nodeToDelete.leftnode == None: #Es una rama con una hoja a la der
            nodeToLink = nodeToDelete.rightnode

        else: #Es una rama con hojas en los dos lados
            highestLowestNode = searchHighestLowestNode(nodeToDelete)
            #print(highestLowestNode.value)
            if nodeToDelete.rightnode != highestLowestNode:
                highestLowestNode.parent.leftnode = None # desvinculo el menor de los mayores
            else:
                nodeToDelete.rightnode = None
            highestLowestNode.leftnode = nodeToDelete.leftnode 
            highestLowestNode.rightnode = nodeToDelete.rightnode
            nodeToLink = highestLowestNode
            #print("L  " + str(highestLowestNode.leftnode.value))
            #print("R  " + str(highestLowestNode.rightnode.value))

        linkNodes(B, parentNode, nodeToDelete, nodeToLink)
        return nodeToDelete.key
    else:
        return None



# deleteKey(B,key)
# Descripción: Elimina una clave del TAD árbol binario.
# Poscondición: Se debe desvincular el Node a eliminar.
# Entrada: el árbol binario B sobre el cual se quiere realizar la
# eliminación (BinaryTree) y el valor de la clave (key) a eliminar.
# Salida: Devuelve clave (key) a eliminar. Devuelve None si el elemento
# a eliminar no se encuentra.

def deleteKey(B, key):

    elementValue = access(B, key)

    if B.root != None and elementValue != None:
        return delete(B, elementValue)
    else:
        return None

# access(B,key)
# Descripción: Permite acceder a un elemento del árbol binario con una
# clave determinada.
# Entrada: El árbol binario (BinaryTree) y la key del elemento al cual
# se quiere acceder.
# Salida: Devuelve el valor de un elemento con una key del árbol
# binario, devuelve None si no existe elemento con dicha clave.

def accessR(currentNode, key):
    if currentNode != None:
        if currentNode.key != key:
            if key < currentNode.key:
                return accessR(currentNode.leftnode, key)
            else:
                return accessR(currentNode.rightnode, key)
        else:
            return currentNode.value
    else:
        return None

def access(B, key):
    if B.root != None:
        return accessR(B.root, key)
    else:
        return None


# update(L,element,key)
# Descripción: Permite cambiar el valor de un elemento del árbol binario
# con una clave determinada.
# Entrada: El árbol binario (BinaryTree) y la clave (key) sobre la cual
# se quiere asignar el valor de element.
# Salida: Devuelve None si no existe elemento para dicha clave. Caso
# contrario devuelve la clave del nodo donde se hizo el update.

def updateR(currentNode, element, key):
    if currentNode.key != key:
        if key < currentNode.key:
            return updateR(currentNode.leftnode, element, key)
        else:
            return updateR(currentNode.rightnode, element, key)
    else:
        currentNode.value = element
        return currentNode.key

def update(B, element, key):
    if access(B, key) != None:
        return updateR(B.root, element, key)
    else:
        return None

def showTreeR(currentNode, side):

    if currentNode != None :
        print("[" + side + " " + str(currentNode.value) + ", " + str(currentNode.key) + "]")
        if currentNode.leftnode != None:
            showTreeR(currentNode.leftnode, "L")
        if currentNode.rightnode != None:
            showTreeR(currentNode.rightnode, "R")
    else:
        print("[]")

def showTree(B):
    if B.root != None:
        return showTreeR(B.root, "ROOT")
    else:
        print("[]")


