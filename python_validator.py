#!/usr/bin/env python3
"""
Validador de sintaxis Python para n8n
Lee código Python desde stdin y valida la sintaxis usando ast.parse
"""

import sys
import json
import ast

def validate_python_code(code):
    """
    Valida código Python usando el parser AST
    Retorna dict con resultados de validación
    """
    try:
        # Validar sintaxis usando AST
        ast.parse(code)
        return {
            "valid": True,
            "error": None,
            "details": "Syntax is valid",
            "method": "python_ast"
        }
    except SyntaxError as e:
        # Extraer información del error de sintaxis
        error_info = {
            "lineno": e.lineno,
            "offset": e.offset,
            "text": e.text.strip() if e.text else None,
            "msg": e.msg
        }
        
        return {
            "valid": False,
            "error": f"Syntax error at line {e.lineno}: {e.msg}",
            "details": error_info,
            "method": "python_ast"
        }
    except Exception as e:
        return {
            "valid": False,
            "error": f"Validation error: {str(e)}",
            "details": str(e),
            "method": "python_ast"
        }

def main():
    """
    Función principal - lee desde stdin, valida, escribe a stdout
    """
    try:
        # Leer toda la entrada estándar
        input_data = sys.stdin.read()
        
        if not input_data:
            result = {
                "valid": False,
                "error": "No input data received",
                "details": "Empty stdin"
            }
        else:
            # Parsear JSON de entrada
            data = json.loads(input_data)
            code = data.get("code", "")
            
            if not code:
                result = {
                    "valid": False,
                    "error": "No Python code provided",
                    "details": "Empty code string in input"
                }
            else:
                # Validar el código
                result = validate_python_code(code)
        
        # Escribir resultado como JSON a stdout
        print(json.dumps(result, ensure_ascii=False))
        
    except json.JSONDecodeError as e:
        error_result = {
            "valid": False,
            "error": f"Invalid JSON input: {str(e)}",
            "details": f"Input received: {input_data[:200]}..."
        }
        print(json.dumps(error_result, ensure_ascii=False))
        
    except Exception as e:
        error_result = {
            "valid": False,
            "error": f"Processor error: {str(e)}",
            "details": str(e)
        }
        print(json.dumps(error_result, ensure_ascii=False))
        sys.exit(1)

if __name__ == "__main__":
    main()