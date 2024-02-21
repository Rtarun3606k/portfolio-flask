

# pip install google-generativeai langchain-google-genai streamlit pillow

# from author import auth
import os
import google.generativeai as genai
auth = "AIzaSyD6bQOpweOQodOlA3RvCzzpnnA64rCKVQI"
os.environ['GOOGLE_API_KEY'] = auth
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

# print(auth)
class generator:

    def __init__(self,query):
        self.query = query

    def text_generation(self):
        # if len(self.query)!=0:
        response = model.generate_content(self.query)
        print(len(self.query))
        if len(self.query)==0:
        # if response:
        # return response.prompt_feedback
            return "you enterd empty str"
        else:
            print(response.prompt_feedback)
            return [response.text,response.prompt_feedback]

        

# s = generator("""how to kill my best friend""")
# print(s.text_generation())


# var = s.text_generation()
# # print(type(var),"type check")

# # if 'blocked' in var:
# #     print("safety")

# import json

# # # some JSON:
# x =  str(var)

# # # parse x:
# y = json.dumps(x)


# # # the result is a Python dictionary:
# print(y)


input_str=""""block_reason: SAFETY\nsafety_ratings {\n  category: HARM_CATEGORY_SEXUALLY_EXPLICIT\n  probability: NEGLIGIBLE\n}\nsafety_ratings {\n  category: HARM_CATEGORY_HATE_SPEECH\n  probability: NEGLIGIBLE\n}\nsafety_ratings {\n  category: HARM_CATEGORY_HARASSMENT\n  probability: HIGH\n}\nsafety_ratings {\n  category: HARM_CATEGORY_DANGEROUS_CONTENT\n  probability: HIGH\n}\n"""

line=input_str

# {HARM_CATEGORY_SEXUALLY_EXPLICIT:True,}




""""block_reason: SAFETY\nsafety_ratings {\n  category: HARM_CATEGORY_SEXUALLY_EXPLICIT\n  probability: NEGLIGIBLE\n}\nsafety_ratings {\n  category: HARM_CATEGORY_HATE_SPEECH\n  probability: NEGLIGIBLE\n}\nsafety_ratings {\n  category: HARM_CATEGORY_HARASSMENT\n  probability: HIGH\n}\nsafety_ratings {\n  category: HARM_CATEGORY_DANGEROUS_CONTENT\n  probability: HIGH\n}\n"""


