#!/usr/bin/env python3
import sys
import json
import ast

def validate_python_code(code):
    try:
        if not code.strip():
            return {
                'valid': False, 
                'error': 'Empty code snippet', 
                'method': 'python_ast',
                'details': {'empty_code': True}
            }
        
        ast.parse(code)
        return {
            'valid': True, 
            'error': None, 
            'method': 'python_ast',
            'details': {'ast_valid': True}
        }

    except SyntaxError as e:
        return {
            'valid': False, 
            'error': f'SyntaxError: Line {e.lineno}: {e.msg}', 
            'method': 'python_ast',
            'details': {
                'syntax_error': True,
                'line_number': e.lineno,
                'error_message': e.msg
            }
        }
    except Exception as e:
        return {
            'valid': False, 
            'error': f'Validation error: {str(e)}', 
            'method': 'python_ast',
            'details': {'general_error': True, 'error_type': type(e).__name__}
        }

if __name__ == "__main__":
    try:
        input_data = sys.stdin.read()
        data = json.loads(input_data)
        code = data.get('code', '')
        result = validate_python_code(code)
        print(json.dumps(result))
    except Exception as e:
        print(json.dumps({
            'valid': False,
            'error': f'Processing error: {str(e)}',
            'method': 'external_script',
            'details': {'script_error': True}
        }))