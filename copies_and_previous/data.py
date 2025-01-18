class HL7Object:
    def __init__(self, obj=None):
        # Initialize a dictionary attribute
        self.data = {}
        
        if obj is not None:
            # If an object (or dictionary) is provided, use it to populate the dictionary
            if isinstance(obj, dict):
                self.data.update(obj)
            else:
                raise ValueError("obj must be a dictionary")
    
    def add_item(self, key, value):
        self.data[key] = value
        
    def get_item(self, key):
        return self.data.get(key, None)
    
    def display(self):
        return self.data