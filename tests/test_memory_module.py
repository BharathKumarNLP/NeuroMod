import unittest
from neuromod.memory_module import HippocampalMemory

class TestHippocampalMemory(unittest.TestCase):
    def test_store_and_recall(self):
        memory = HippocampalMemory()
        memory.store_short_term("Sample data")
        memory.commit_to_long_term("key1", "Important info")

        self.assertEqual(memory.recall("key1"), "Important info")
        self.assertEqual(memory.recall("unknown"), "Memory not found")

if __name__ == "__main__":
    unittest.main()

