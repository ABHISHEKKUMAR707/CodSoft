from flask import Flask, render_template, request, jsonify, session
from calculator import Calculator, add_two_numbers

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Global calculator instance for session management
def get_calculator():
    """Get or create calculator instance for current session"""
    if 'calculator_id' not in session:
        session['calculator_id'] = 'default'
    
    if not hasattr(app, 'calculators'):
        app.calculators = {}
    
    if session['calculator_id'] not in app.calculators:
        app.calculators[session['calculator_id']] = Calculator()
    
    return app.calculators[session['calculator_id']]

@app.route('/')
def index():
    """Redirect to calculator page"""
    return render_template('calculator.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    """Handle calculator operations with complete operation tracking"""
    calc = get_calculator()
    
    if request.method == 'GET':
        return render_template('calculator.html', history=calc.get_history())
    
    if request.method == 'POST':
        try:
            # Get form data
            num1 = request.form.get('num1')
            num2 = request.form.get('num2')
            operation = request.form.get('operation', 'add')
            
            # Validate input
            if not num1 or not num2:
                return render_template('calculator.html', 
                                     error="Please enter both numbers",
                                     history=calc.get_history())
            
            # Perform calculation based on operation
            if operation == 'add':
                result_detail = calc.add(num1, num2)
            elif operation == 'subtract':
                result_detail = calc.subtract(num1, num2)
            elif operation == 'multiply':
                result_detail = calc.multiply(num1, num2)
            elif operation == 'divide':
                result_detail = calc.divide(num1, num2)
            else:
                return render_template('calculator.html', 
                                     error="Invalid operation selected",
                                     history=calc.get_history())
            
            return render_template('calculator.html', 
                                 result=result_detail,
                                 history=calc.get_history())
            
        except ZeroDivisionError:
            return render_template('calculator.html', 
                                 error="Error: Division by zero is not allowed",
                                 history=calc.get_history())
        except ValueError as e:
            return render_template('calculator.html', 
                                 error=f"Error: {str(e)}",
                                 history=calc.get_history())
        except Exception as e:
            return render_template('calculator.html', 
                                 error="An unexpected error occurred. Please try again.",
                                 history=calc.get_history())

@app.route('/calculator/history')
def calculator_history():
    """Get calculator history as JSON"""
    calc = get_calculator()
    return jsonify(calc.get_history())

@app.route('/calculator/clear', methods=['POST'])
def clear_calculator_history():
    """Clear calculator history"""
    calc = get_calculator()
    calc.clear_history()
    return render_template('calculator.html', 
                         message="History cleared successfully",
                         history=calc.get_history())

@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    """API endpoint for calculator operations"""
    calc = get_calculator()
    
    try:
        data = request.get_json()
        num1 = data.get('num1')
        num2 = data.get('num2')
        operation = data.get('operation', 'add')
        
        if num1 is None or num2 is None:
            return jsonify({'error': 'Both num1 and num2 are required'}), 400
        
        # Perform calculation
        if operation == 'add':
            result_detail = calc.add(num1, num2)
        elif operation == 'subtract':
            result_detail = calc.subtract(num1, num2)
        elif operation == 'multiply':
            result_detail = calc.multiply(num1, num2)
        elif operation == 'divide':
            result_detail = calc.divide(num1, num2)
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
        return jsonify({
            'success': True,
            'result': result_detail,
            'history_count': len(calc.get_history())
        })
        
    except ZeroDivisionError:
        return jsonify({'error': 'Division by zero is not allowed'}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)