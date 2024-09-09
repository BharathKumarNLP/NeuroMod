import unittest
from neuromod.attention_module import AttentionMechanism, clear_attention_weights

class TestAttentionModule(unittest.TestCase):
    
    def setUp(self):
        """Setup a fresh AttentionMechanism instance before each test."""
        self.attention_mechanism = AttentionMechanism()
    
    def test_apply_attention(self):
        """Test applying attention with specific weights."""
        inputs = [1, 2, 3]
        weights = [0.1, 0.2, 0.3]
        result = self.attention_mechanism.apply_attention(inputs, weights)
        self.assertEqual(result, 1.4)  # (1*0.1 + 2*0.2 + 3*0.3)
    
    def test_set_weights(self):
        """Test setting attention weights."""
        result = self.attention_mechanism.set_weights("key1", [0.1, 0.2, 0.3])
        self.assertEqual(result, "Weights Set")
        self.assertEqual(self.attention_mechanism.attention_weights["key1"], [0.1, 0.2, 0.3])
    
    def test_clear_attention_weights(self):
        """Test clearing attention weights."""
        self.attention_mechanism.set_weights("key1", [0.1, 0.2, 0.3])
        result = clear_attention_weights(self.attention_mechanism)
        self.assertEqual(result, "Attention Weights Cleared")
        self.assertEqual(self.attention_mechanism.attention_weights, {})
    
if __name__ == "__main__":
    unittest.main()

