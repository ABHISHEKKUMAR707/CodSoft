from flask import Flask, render_template, request, flash
from calculator import add_two_numbers

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'

@app.route('/')
def index():
    """Redirect to calculator page"""
    return render_template('calculator.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    """Handle calculator operations"""
    if request.method == 'GET':
        return render_template('calculator.html')
    
    if request.method == 'POST':
        try:
            # Get form data
            num1 = request.form.get('num1')
            num2 = request.form.get('num2')
            
            # Validate input
            if not num1 or not num2:
                return render_template('calculator.html', 
                                     error="Please enter both numbers")
            
            # Convert to numbers and calculate
            result = add_two_numbers(num1, num2)
            
            return render_template('calculator.html', result=result)
            
        except ValueError as e:
            return render_template('calculator.html', 
                                 error=f"Error: {str(e)}")
        except Exception as e:
            return render_template('calculator.html', 
                                 error="An unexpected error occurred. Please try again.")

if __name__ == '__main__':
    app.run(debug=True)