import linkedlist
import algo1

class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []       # lista de claves (ordenadas)
        self.children = []   # lista de hijos (len(children) = len(keys)+1 si no es hoja)
        self.leaf = leaf

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(leaf=True)
        self.t = t   # grado mínimo


# INSERT: 

def insert(BTree, key):
    if BTree.root == None: 
        BTree.root = BTreeNode(leaf=True)
        BTree.root.keys.append(key)
    elif len(BTree.root.keys) == 2*BTree.t - 1:
        newRoot = BTreeNode(leaf=False)
        newRoot.children.append(BTree.root)
        splitChild(newRoot, 0)
        BTree.root = newRoot
        insertNonFull(BTree.root, key)
    else:
        insertNonFull(BTree.root, key)

def insertNonFull(node, key):
    if node.leaf == True:
        node.keys.append(key)
        node.keys.sort()
    else: 
        # Encontrar la posición correcta para insertar la clave
        i = len(node.keys) - 1
        while i >= 0 and key < node.keys[i]:
            i -= 1
        i += 1  # i ahora apunta al hijo correcto
        
        # Verificar si el hijo está lleno (tiene 2t-1 claves)
        if len(node.children[i].keys) == 2*BTree.t - 1:
            splitChild(node, i)  # Dividir el hijo lleno
            # Si la clave es mayor que la clave media que subió, ir al hijo derecho
            if key > node.keys[i]:
                i += 1
        
        # Insertar recursivamente en el hijo apropiado
        insertNonFull(node.children[i], key)

def splitChild(parent, index):
    # Obtener el hijo lleno que vamos a dividir
    fullChild = parent.children[index]
    
    # Crear el nuevo nodo derecho
    rightChild = BTreeNode(leaf=fullChild.leaf)
    
    # La clave media es la que está en la posición t-1 (medio del array)
    t = len(fullChild.keys) // 2 + 1  # grado mínimo
    middleKey = fullChild.keys[t-1]
    
    # Mover las claves mayores a la mitad al nodo derecho
    rightChild.keys = fullChild.keys[t:]  # desde t hasta el final
    
    # Si no es hoja, también mover los hijos
    if not fullChild.leaf:
        rightChild.children = fullChild.children[t:]  # hijos desde t hasta el final
    
    # Truncar el hijo izquierdo (quedarse solo con las primeras t-1 claves)
    fullChild.keys = fullChild.keys[:t-1]  # desde 0 hasta t-1
    if not fullChild.leaf:
        fullChild.children = fullChild.children[:t]  # hijos desde 0 hasta t
    
    # Subir la clave media al padre
    parent.keys.insert(index, middleKey)  # insertar en la posición index
    
    # Insertar el nuevo nodo derecho como hijo del padre
    parent.children.insert(index + 1, rightChild)  # insertar después de la clave media
        



# Ejercicio 4:   
# Diseñe e implemente un algoritmo 
# que reciba como entrada un B-Tree y 
# devuelva la clave mínima almacenada en el B-tree.

def findMin(BTree):
    if BTree.root == None: 
        return None
    return findMinR(BTree.root)

def findMinR(node):

    if node.leaf == False: 
        return findMinR(node.children[0])
    else: 
        return node.keys[0]


# Ejercicio 5:   
# Diseñe e implemente un algoritmo que reciba como entrada un 
# B-Tree y una clave k y devuelva el predecesor de k dentro del 
# B-Tree. En caso de no existir el predecesor de k dentro del 
# B-tree devolver None.

def findKey(BTree, k):
    if BTree.root == None: 
        return None
    return findKeyR(BTree.root, k)

def findKeyR(node, k):
    # Buscar la clave k en el nodo actual
    for i in range(len(node.keys)):
        if node.keys[i] == k:
            return (node, i)  # Encontramos k, devolvemos nodo y posición
        elif k < node.keys[i]:
            # k es menor que la clave actual, ir al hijo izquierdo
            if node.leaf == False: 
                return findKeyR(node.children[i], k)  # children[i] contiene claves < node.keys[i]
            else: 
                return None  # Es hoja y no encontramos k
    
    # k es mayor que todas las claves del nodo, ir al último hijo
    if node.leaf == False: 
        return findKeyR(node.children[-1], k)  # children[-1] contiene claves > todas las del nodo
    else: 
        return None  # Es hoja y no encontramos k
     

def findPredecessor(BTree, k): 
    if BTree.root == None: 
        return None
    
    (node, i) = findKey(BTree, k)

    if node == None: 
        return None 
    elif findMin(BTree) == k: 
        return None
    else: 
        if i > 0: 
            return node.keys[i-1]
        else: 
            if len(node.children) > 0 and len(node.children[0].keys) > 0: 
                return node.children[0].keys[-1]

# Ejercicio 6:   
# Diseñe e implemente un algoritmo que reciba como entrada 
# un B-Tree y un entero k y devuelva True si existen dos 
# claves en el B-tree que sumen k

def hasTwoSum(BTree, k):
    if BTree.root == None: 
        return False 
    else: 
        keys = extractKeysLessThan(BTree, k)
        return findTwoSum(keys, k)

def extractKeysLessThan(BTree, k):
    if BTree.root == None: 
        return None 
    else: 
        return extractKeysLessThanR(BTree.root, k)

def extractKeysLessThanR(node, k):
    result = []

    for key in node.keys:
        if key < k:
            result.append(key)

    if node.leaf == False: 
        for child in node.children:
            childKeys = extractKeysLessThanR(child, k)
            result.extend(childKeys)

    return result

def findTwoSum(keys, k): 

    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            if keys[i] + keys[j] == k:
                return True 
    return False 