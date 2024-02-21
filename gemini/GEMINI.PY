import os
import google.generativeai as genai
import time  # Import the time module
# from .auth import api_key
# from gemini import *
from auth import api_key


os.environ['GOOGLE_API_KEY'] = api_key
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')
class generate:
    def __init__(self,query):
        self.query=query

    def process(self):
            x=self.query
            start_time = time.time()  # Mark the start time
            response = model.generate_content(x)

            end_time = time.time()  # Mark the end time
            processing_time = end_time - start_time  # Calculate the processing time
            text = ''
            try:
                text=response.text
                text = str(text)

                # print(text)
                print("Processing time:", int(processing_time), "seconds")  # Print the processing time
            except:

                text ="Sorry i am not supposed to answer that kind of questions"
            return text

    # def __repr__: 
    #     return s
# s = generate("kill")
# print(s.process())
# s.process()