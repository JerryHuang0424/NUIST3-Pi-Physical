import RPi.GPIO as GPIO
import time

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
		""",
		"""4. The best structure for implementing a multi-way decision in Python is:
			a. if
			b. if-else
			c. if-elif-else
			d. try
		""",
		"""5. What statement can be executed in the body of a loop to cause it to terminate?
			a. if
			b. exit
			c. continue
			d. break
		"""
	]

	answers = [
		"c",
		"d",
		"d",
		"c",
		"d"
	]

	score = 0

	#Ask questions

	for i in range(len(questions)):
		user_answer = input(questions[i]).strip().lower()
		if user_answer == answers[i]:
			print("Correct!")
			score += 1
			print("LED ON")
			GPIO.output(17,GPIO.HIGH)
			time.sleep(1)
			print("LED off")
			GPIO.output(17,GPIO.LOW)
			
		else:
			print("Incorrect!")
			print("LED ON")
			GPIO.output(18,GPIO.HIGH)
			time.sleep(1)
			print("LED off")
			GPIO.output(18,GPIO.LOW)

	# Provide final score
	print("Quiz completed!")
	print(f"You got {score}/{len(questions)} questions correct.")
	
# Run the quiz function

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
quiz()


