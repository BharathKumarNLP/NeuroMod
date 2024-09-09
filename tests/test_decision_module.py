import unittest
from neuromod.decision_module import DecisionMaker, reset_decisions

class TestDecisionModule(unittest.TestCase):
    
    def setUp(self):
        """Setup a fresh DecisionMaker instance before each test."""
        self.decision_maker = DecisionMaker()
    
    def test_make_decision(self):
        """Test making a decision."""
        decision = self.decision_maker.make_decision("context1", "option1")
        self.assertEqual(decision, "option1")
    
    def test_make_decision_overwrite(self):
        """Test decision overwrite based on context."""
        self.decision_maker.make_decision("context1", "option1")
        decision = self.decision_maker.make_decision("context1", "option2")
        self.assertEqual(decision, "option1")
    
    def test_reset_decisions(self):
        """Test resetting decisions."""
        self.decision_maker.make_decision("context1", "option1")
        result = reset_decisions(self.decision_maker)
        self.assertEqual(result, "Decisions Reset")
        self.assertEqual(self.decision_maker.decisions, {})
    
if __name__ == "__main__":
    unittest.main()


