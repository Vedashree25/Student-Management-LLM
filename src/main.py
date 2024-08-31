# src/main.py
from supervisor import Supervisor
from adapter import Adapter
from llm_layer import LLMLayer

def main():
    # Initialize components
    llm_layer = LLMLayer(model_name="gpt2")  # Use appropriate model
    adapter = Adapter(llm_layer)
    supervisor = Supervisor(adapter)

    # Example interaction
    user_query = "What books do you recommend for machine learning?"
    response = supervisor.handle_query(user_query)
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
    
    # Example interaction with logging
    user_query = "What books do you recommend for machine learning?"
    
    # Log the user query
    logging.info(f"User Query: {user_query}")
    
    # Process the query
    response = supervisor.process_student_query(user_query)
    
    # Log the agent's response
    logging.info(f"Agent Response: {response}")
    
    # Print the response to the console
    print("Agent Response:", response)

if __name__ == "__main__":
    main()

