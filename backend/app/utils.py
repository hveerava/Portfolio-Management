from datetime import datetime

def format_date(date_str):
    """Format a date string to a specific format."""
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%B %d, %Y')
    except ValueError:
        return None

def validate_investment_type(investment_type):
    """Validate the investment type."""
    valid_types = ['stock', 'bond', 'real estate', 'cash']
    return investment_type in valid_types

def api_response(success, data=None, message=None):
    """Standardize API response format."""
    response = {
        'success': success,
        'data': data,
        'message': message
    }
    return response

def parse_date(date_str):
    """Parse a date string to a datetime object."""
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return None

def calculate_return(initial_investment, final_value):
    """Calculate the return on investment."""
    try:
        return ((final_value - initial_investment) / initial_investment) * 100
    except ZeroDivisionError:
        return None
