import google.generativeai as palm
def bot_prompt(prompt):
        API_KEY = "AIzaSyDdHep_5mRJhFd_XT7Qs0lI512vK1wL64Y"
        palm.configure(api_key = API_KEY)
        response=palm.chat(messages=prompt,temperature=0.2,context="Speak like a Doctor assistance")
        return response