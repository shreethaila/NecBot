from chatterbot import ChatBot as BaseChatBot
from chatterbot.conversation import Statement
from fuzzywuzzy import fuzz

class CustomChatBot(BaseChatBot):
    def __init__(self, name, conversation_list, threshold=70, default_response="Hi there, If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br><br>", **kwargs):
        super().__init__(name, **kwargs)
        self.conversation_list = conversation_list
        self.threshold = threshold
        self.default_response = default_response
        self.context = None 

    def get_response(self, statement, **kwargs):
        
        statement_text = statement.lower()

       
        best_match = None
        best_score = 0

        
        response_dict = {}

        
        for i in range(0, len(self.conversation_list), 2):
            query = self.conversation_list[i].lower()
            response = self.conversation_list[i + 1]

            
            score = fuzz.partial_ratio(query, statement_text)

           
            response_dict[query] = (response, score)

            
            if self.context and query in self.context:
                score += 10 

            if score > best_score:
                best_score = score
                best_match = query

        
        self.context = statement_text

       
        if best_match and best_score >= self.threshold:
            return Statement(text=response_dict[best_match][0], confidence=best_score)

        
        return Statement(text=self.default_response, confidence=0)
