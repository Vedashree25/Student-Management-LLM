class Adapter:
    def __init__(self, llm_layer):
        self.llm_layer = llm_layer

    def process_query(self, user_query, context):
        formatted_query = f"User: {user_query}"
        response = self.llm_layer.get_response(formatted_query, context)
        return response
 
