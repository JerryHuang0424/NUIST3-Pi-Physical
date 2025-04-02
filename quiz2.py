# NUist Quiz Game in Python
def quiz():
	print("Welcome to the Animal Quiz")
	print("Answer the following question:")

	# Question and Answers
	questions = [
		"""1. which of the following is NOT a python data type?
			a.int 
			b. float
			c. rational
			d. string
			e. bool
			""",
		"""2. WHich of the following is NOT a built-in operation in Python?
			a. +
			b. %
			c. abs()
			d. sqrt()
		""",
		"""3. In a mixed type expression involving ints and floats, Python will convert:
			a. floats to ints
			b. ints to strings
			c. floats and ints to strings
			d. ints to floats
		"""
	]

	answers = [
		"c",
		"d",
		"d"
	]

	score = 0

	#Ask questions

	for i in range(len(questions)):
		user_answer = input(questions[i]).strip().lower()
		if user_answer == answers[i]:
			print("Correct!")
			score += 1
		else:
			print("Incorrect!")

	# Provide final score
	print("Quiz completed!")
	print(f"You got {score}/{len(questions)} questions correct.")
	
# Run the quiz function
quiz()


