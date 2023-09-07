class DialogueHistory:
    def __init__(self):
        self.history = ""

    def add_history(self, dialogue):
        self.history += dialogue
        if len(self.history) > 1000:
            self.history = self.history[-1000:]

    def get_history(self):
        return self.history
