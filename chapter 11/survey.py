class AnonymousSurvey:
    """调查问卷"""

    def __init__(self,question):
        """存储问题和答案"""
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self,new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results")
        for response in self.responses:
            print(f"- {response}")
