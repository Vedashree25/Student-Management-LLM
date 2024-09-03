class Supervisor:
    def __init__(self, adapter):
        self.adapter = adapter

    def query(self, user_query):
        context = {}
        response = self.adapter.process_query(user_query, context)
        return response

    def follow_up_query(self, user_query, context):
        response = self.adapter.process_query(user_query, context)
        return response
