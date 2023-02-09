from survey import AnonymousSurvey

#Definite question with create instance AnonymousSurvey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)


#Display questuon and save responses.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

   
#Display results of survey.
print("\nThank you to everyone who partcipated in the survey!")
my_survey.show_results()


