class HippocampalMemory:
    def __init__(self):
        self.short_term_memory = []
        self.long_term_memory = {}

    def store_short_term(self, data):
        self.short_term_memory.append(data)

    def commit_to_long_term(self, identifier, data):
        self.long_term_memory[identifier] = data

    def recall(self, identifier):
        return self.long_term_memory.get(identifier, "Memory not found")

    def clear_memory(self):
        self.short_term_memory.clear()
        self.long_term_memory.clear()

