from FilaArray import FilaArray

class SetWithQueue:
    def __init__(self):
        self.fila = FilaArray()

    def contains(self, item):
        for i in range(len(self.fila)):
            current_index = (self.fila._inicio + i) % len(self.fila._dados)
            
            if self.fila._dados[current_index] == item:
                return True 
        
        return False
    
    def add(self, item):
        if not self.contains(item):
            self.fila.enqueue(item)
            
    def remove(self, item):
        if not self.contains(item):
            raise ValueError("Element not found")
        
        temp_fila = FilaArray()
        found = False
        
        for i in range(len(self.fila)):
            current_item = self.fila._dados[(self.fila._inicio + i) % len(self.fila._dados)]
            if current_item == item and not found:
                found = True 
            else:
                temp_fila.enqueue(current_item)
        
        self.fila = temp_fila  
        
    def size(self):
        return len(self.fila)
    
    def list(self):
        return [self.fila._dados[(self.fila._inicio + i) % len(self.fila._dados)] for i in range(len(self.fila))]
