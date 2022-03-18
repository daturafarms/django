from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "input.html")

# simple function for addition
def addition(request):

	number1 = request.POST['number1']
	number2 = request.POST['number2']
	if number1.isdigit() and number2.isdigit():
		x = int(number1)
		y = int(number2)
		stk = x + y
# I don't need to go over x + y hopefully
		return render(request, "answer.html", {"answer": stk})
	else:
		stk = "Only digits are allowed"
		return render(request, "answer.html", {"answer": stk})

def subtract(request):

	number1 = request.POST['number1']
	number2 = request.POST['number2']
# simple subtration function	
	if number1.isdigit() and number2.isdigit():
		x = int(number1)
		y = int(number2)
		stk = x - y
# again, would explain better, but not needed for X - Y

		return render(request, "answer.html", {"answer": stk})

def multiply(request):

	number1 = request.POST['number1']
	number2 = request.POST['number2']
# simple multiplication function, again no explanation needed
	if number2.isdigit () and number2.isdigit():
		x = int(number1)
		y = int(number2)
		stk = x * y
# render answer in HTML
		return render(request, "answer.html", {"answer": stk})
	else:
		stk = "Only numbers are allowed"
		return render(request, "answer.html", {"result": stk})


def divide(request):

	number1 = request.POST['number1']
	number2 = request.POST['number2']

	if number1. isdigit() and number2.isdigit():
		x = int(number1)
		y= int(number2)

		if y == 0:
			stk = "Divide by zero error"
			return render(request, "answer.html", {"answer": stk})
		else:
			stk = x / y
			return render(request, "answer.html", {"answer": stk})

	else:
	    
		stk = "Only numbers are allowed"
		return render(request, "answer.html", {"answer": stk})
