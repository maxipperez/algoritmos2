import LinkedList

class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False

# Para manejar múltiples nodos,
# el campo children contiene una estructura 
# LinkedList conteniendo TrieNode

# insert(T,element) 
# Descripción: insert un elemento en T, siendo T un Trie.
# Entrada: El Trie sobre la cual se quiere agregar el elemento 
# (Trie)  y el valor del elemento (palabra) a  agregar.
# Salida: No hay salida definida

def insert(T,element):
    if T.root == None: 
        T.root = TrieNode()
        T.root.children = LinkedList()
    insertR(T.root,element,0)

def insertR(node,word,index):
    if index >= len(word): 
        node.isEndOfWord = True 
        return 

    currentChar = word[index]
    existingNode = searchNode(node.children, currentChar)

    if existingNode == None: 
        newTrieNode = TrieNode()
        newTrieNode.key = currentChar
        newTrieNode.children = LinkedList()
        add(node.children, newTrieNode)
        insertR(newTrieNode, word, index + 1)
    else: 
        insertR(existingNode, word, index + 1)

def searchNode(L, element): 
    current = L.head
    while current != None:
        if current.value.key == element:
            return current.value
        current = current.nextNode
    return None

# search(T,element)
# Descripción: Verifica que un elemento se encuentre dentro del Trie
# Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie)  
# y el valor del elemento (palabra)
# Salida: Devuelve False o True  según se encuentre el elemento.

def search(T,element): 
    if T.root == None: 
        return False 
    return searchR(T.root, element, 0)

def searchR(node,word,index):
    if index >= len(word):
        if node.isEndOfWord == True: 
            return True 
        else: 
            return False 
    
    currentChar = word[index]
    existingNode = searchNode(node.children, currentChar)
    
    if existingNode == None: 
        return False
    else: 
        return searchR(existingNode, word, index + 1)

# delete(T,element)
# Descripción: Elimina un elemento se encuentre dentro del Trie
# Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie)  
# y el valor del elemento (palabra) a  eliminar.
# Salida: Devuelve False o True  según se haya eliminado el elemento.

def delete(T,element): 
    if T.root == None: 
        return False 
    return deleteR(T.root, element, 0)

def deleteR(node, word, index): 
    if index >= len(word): 
        if node.isEndOfWord == True: 
            node.isEndOfWOrd == False
            return True 
        else: 
            return False 
    
    currentChar = word[index]
    existingNode = searchNode(node.childre, currentChar)

    if existingNode == None: 
        return False 

    result = deleteR(existingNode, word, index + 1)

    if result != None and node.children.head == None and node.isEndOfWord == False: 
        removeNodeFromChildren(node.parent, node)

def removeNodeFromChildren(parentNode, nodeToRemove): 
    current = parentNode.children.head
    prev = None 

    while current != None: 
        if current.value == nodeToRemove: 
            if prev == None: 
                parentNode.children.head = current.nextNode 
            else: 
                prev.nextNode = current.nextNode 
            return True 
        prev = current 
        current = current.nextNode 
    return False 

    
