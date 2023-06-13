from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, InternalServerError
from swiplserver import PrologMQI, PrologThread
import json

app = Flask(__name__)
CORS(app)

# Serve static files from the root directory
@app.route('/logo.png', methods=['GET'])
def serve_files():
    return send_from_directory('.', 'logo.png')

@app.route('/.well-known/ai-plugin.json', methods=['GET'])
def serve_ai_plugin():
    return send_from_directory('.well-known', 'ai-plugin.json')

@app.route('/openapi.yaml', methods=['GET'])
def serve_openapi():
    return send_from_directory('.', 'openapi.yaml')

@app.route('/compile', methods=['POST'])
def compile_code():
    try:
        data = request.get_json(force=True)
        
        # Extract the 'code' from the request JSON
        code = data['code']

        print("Request:", request.method, request.path, data)  # Print the request to the console
        print("Code: ", code)

        # Save code to file so it can be compiled.
        with open("code.pl", "w") as file:
            # Write the string to the file
            file.write(code)
        
        with PrologMQI() as mqi:
            with mqi.create_thread() as prolog_thread:  
                result = prolog_thread.query('[compile]')        
                print(result)        
                errors = prolog_thread.query('compile:compile(Errors)')             
                print(errors)
                error_message = []
                try:
                    error_message = errors[0]['Errors'][0]['args'][1]
                except (IndexError, KeyError):
                    pass
   
        response = {
            'success': True,
            'Errors': error_message
        }
        
        return jsonify(response), 200
    
    except BadRequest:
        return jsonify({'error': 'Invalid request'}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
