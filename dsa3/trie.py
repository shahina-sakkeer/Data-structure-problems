class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=TrieNode()         #root is also has its children.it is also a node


    def insert(self,word):
        current=self.root

        for ch in word:
            if ch not in current.children:         #check wheather the root/node has already dont have this character has its children
                current.children[ch]=TrieNode()         #if no, current-->children add that ch as key and its node as value.OR add this character as a key and create a new TrieNode as its value. current.children[ch]  means ipozhathe currentinte children aaya ch inte value

            current=current.children[ch]         #move to current to its child node
            
        current.end=True        #if the loop is over, mark that word as end 


    def search(self,word):
        current=self.root

        for ch in word:
            if ch not in current.children:          #checking wheather the current--->children dictionary carries any key of ch 
                return False
            
            current=current.children[ch]

        return current.end
    

    def autocomplete(self,prefix):        #lets say, prefix="ap"
        current=self.root

        for ch in prefix:
            if ch not in current.children:
                return []
        
            current=current.children[ch]           #why this above steps are needed because dfs starts from the prefix end node. that is, if prefix is "ap", is starts from (node p,ap)

        result=[]
        stack=[(current,prefix)]          #(node p,"ap")

        while stack:
            node,path=stack.pop()         #node=node p and path="ap"
            if node.end:          #if this node marked as end=true, then we got one word
                result.append(path)               #append that word to the result   

            for ch,child in node.children.items():           #it means loop through current node's chiildren key and value. ch and child indicates key and values of node.children
                stack.append((child,path+ch))            #path now has "ap" . to that add next character "p". now child becomes node , path becomes path

        return result


    def display(self):
        stack=[]
        
        stack.append((self.root,""))
        
        while stack:
            node,word=stack.pop()
            
            if node.end:
                print(word)
                
            for ch,child in node.children.items():           #child is the value, ch is the key
                stack.append((child,word+ch))               #word+ch if we write like this only, words will get printed
        

trie=Trie()
trie.insert("app")
trie.insert("apple")
trie.insert("apply")
# print(trie.search("car"))
# print(trie.search("carp"))
# print(trie.search("cart"))
print(trie.autocomplete("app"))
trie.display()