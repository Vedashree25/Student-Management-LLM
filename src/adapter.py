
class Adapter:
    def __init__(self, llm_layer):
        self.llm_layer = llm_layer

    def process_query(self, user_query, context):
        # Format query and send to LLM layer
        formatted_query = f"User asked: {user_query}"
        response = self.llm_layer.get_response(formatted_query, context)
        return response
 
