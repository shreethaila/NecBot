from customchatbot import CustomChatBot
conversation_list = [
    "hi",
    "hello",
    "student",
    "I am a student"
]

custom_bot = CustomChatBot('MyCustomBot', conversation_list)

# Get responses
response1 = custom_bot.get_response("Hi there!")
response2 = custom_bot.get_response("I am a student studying computer science.")
response3 = custom_bot.get_response("How are you?")
print(response1)
print(response2)
print(response3)
