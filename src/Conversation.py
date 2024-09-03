class ConversationManager:
    def __init__(self):
        self.is_follow_up_needed = False
        self.last_response = ""
        self.current_user_input = ""

    def fetch_agent_response(self, user_input):
        response = agent.generate_response(user_input)  
        return response

    def assess_need_for_follow_up(self, response):
        if "specify" in response or "clarify" in response:
            self.is_follow_up_needed = True
        else:
            self.is_follow_up_needed = False

    def create_follow_up_question(self):
        if self.is_follow_up_needed:
            return "Could you provide more details on that?"
        return None

    def continue_conversation(self, user_input):
        response = self.fetch_agent_response(user_input)
        print("Agent:", response)

        self.assess_need_for_follow_up(response)

        if self.is_follow_up_needed:
            follow_up_question = self.create_follow_up_question()
            if follow_up_question:
                print("Agent (Follow-up):", follow_up_question)
                self.current_user_input = input("User: ")

                self.continue_conversation(self.current_user_input)


if __name__ == "__main__":
    conversation_manager = ConversationManager()
    initial_user_input = input("User: ") 
    conversation_manager.continue_conversation(initial_user_input)
