from transformers import pipeline

class LLMLayer:
    def __init__(self, model_name):
        self.model = pipeline('text-generation', model="gpt2") 

    def get_response(self, query, context):
        response = self.model(query, max_length=100)[0]['generated_text']
        return response
 
