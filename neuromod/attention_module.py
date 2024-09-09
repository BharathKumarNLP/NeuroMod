class AttentionModule:
    def __init__(self):
        self.current_focus = None

    def set_attention(self, focus):
        self.current_focus = focus
        print(f"Focus set on: {self.current_focus}")

    def switch_attention(self, new_focus):
        self.current_focus = new_focus
        print(f"Switched attention to: {self.current_focus}")

    def get_current_focus(self):
        return self.current_focus
# This mimics the brain’s ability to switch focus or multitask.
