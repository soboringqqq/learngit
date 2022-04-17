from survey import AnonymousSurvey


question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
	response = input("language: ")
	
	if response == 'q':
		break
	my_survey.store_response(response)
	
print("\n Thank you to everyone who participated in the survey!")
my_survey.show_results()
