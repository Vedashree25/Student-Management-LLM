# src/main.py
from supervisor import Supervisor
from adapter import Adapter
from llm_layer import LLMLayer

def main():
    llm_layer = LLMLayer(model_name="gpt2")
    adapter = Adapter(llm_layer)
    supervisor = Supervisor(adapter)

    # Example interaction
    user_query = "What books to read for AI?"
    response = supervisor.query(user_query)
    print("Agent Response:", response)

if __name__ == "__main__":
    main()

# src/main.py

import logging
from supervisor import Supervisor
from adapter import Adapter
from llm_layer import LLMLayer

# Configure logging
logging.basicConfig(filename='logs/user_interactions.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Create instances of Adapter and LLMLayer
    adapter = Adapter()
    llm_layer = LLMLayer()
    supervisor = Supervisor(adapter, llm_layer)
    
    user_query = "What books to read for AI?"
    
    logging.info(f"User Query: {user_query}")
    
    response = supervisor.process_student_query(user_query)

    logging.info(f"Agent Response: {response}")
    
    print("Agent Response:", response)

if __name__ == "__main__":
    main()

