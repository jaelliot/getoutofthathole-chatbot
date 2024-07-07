# context_manager.py

class ContextManager:
    def __init__(self):
        self.default_context = "Default context information."

    def get_context(self, user_id, conversation_history):
        # Improved logic to retrieve dynamic context based on user_id and conversation history
        dynamic_context = self.default_context
        if conversation_history:
            # Example: append recent messages to context
            dynamic_context += " ".join([msg["content"] for msg in conversation_history[-5:]])
        return dynamic_context
