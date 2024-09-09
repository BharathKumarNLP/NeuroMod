# neuromod/decision_module.py

class DecisionMaker:
    def __init__(self):
        self.decisions = {}

    def make_decision(self, context, option):
        # Simplistic decision-making logic for demonstration
        if context not in self.decisions:
            self.decisions[context] = option
        return self.decisions[context]

def reset_decisions(decision_maker):
    decision_maker.decisions.clear()
    return "Decisions Reset"

