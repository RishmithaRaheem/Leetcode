# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
		self.cache = {}
		self.doubleLinkedList_ofnodes = DoublyLinkedList()
        self.maxSize = maxSize or 1
		self.currentSize = 0
		

    def insertKeyValuePair(self, key, value):
        # Write your code here.
		if key in self.cache: 
			self.replaceKey(key,value)  #value change 
		else:
			if self.maxSize == self.currentSize: #max_size_reached
				self.evictLeastUsed()
			else: #maxzise not reached
				self.currentSize+=1
			self.cache[key] = DoublyLinkedListNode(key,value)
		self.updateMostRecent(self.cache[key]) #whatever the case, this node had to be made the head 
			
	def evictLeastUsed(self):
		key_to_remove = self.doubleLinkedList_ofnodes.tail.key
		self.doubleLinkedList_ofnodes.updateNewTail()
		del self.cache[key_to_remove]
		
		
  

    def getValueFromKey(self, key):
        if key not in self.cache:
			return None
		self.updateMostRecent(self.cache[key])
		return self.cache[key].value
	
	def updateMostRecent(self, node):
		self.doubleLinkedList_ofnodes.setHeadTo(node)

    def getMostRecentKey(self):
		if self.doubleLinkedList_ofnodes.head is None:
			return None
        return self.doubleLinkedList_ofnodes.head.key
	
	def replaceKey(self,key,value):
		if key not in self.cache:
			raise Exception("stupid theres no such key ]")
		self.cache[key].value = value

	

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
	def setHeadTo(self,node): #make this node the head
		if self.head == node: #updation of value. no need head change 
			return 
		elif self.head is None: #no nodes present 
			self.head = node
			self.tail = node
		elif self.head == self.tail: #only one node present 
			node.next = self.head
			self.head.prev = node
			self.head = node
		else:  
			if self.tail == node:
				self.updateNewTail() # tail is updated 
			node.removeBindings() #node remove
			#make this new node the head 
			self.head.prev = node 
			node.next = self.head
			self.head = node
	
	def updateNewTail(self):
			if self.tail is None:
				return 
			elif self.head == self.tail:
				self.head = None
				self.tail = None
				return

			self.tail = self.tail.prev
			self.tail.next = None

				
				
		
class DoublyLinkedListNode:
	def __init__(self,key,value):
		self.key = key
		self.value = value
		self.next = None
		self.prev = None
	
	def removeBindings(self): #deleting a node - a node is removing itself from its connections 
		if self.prev is not None:
			self.prev.next = self.next
		if self.next is not None:
			self.next.prev = self.prev
		self.next = None
		self.prev = None
		
		
