class AnonymousSurvey ():
    """Get anonymous responses."""

    def __init___(self, question):
        """Saves question and ready to save responses."""
    self_question = question
    self.responses = []
    

    def show_question(self):
        """Display the question."""
    print(question)

    def store_response(self, new_response):
        """Save one answer for survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Display all getted responses."""
        print("Survey results:")
        for response in responses:
            print('- ' + response)


