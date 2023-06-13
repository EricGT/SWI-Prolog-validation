# SWI-Prolog-validation
A ChatGPT plugin that will validate Prolog code generated by ChatGPT by compiling the code with SWI-Prolog.

---

To install:

Note: This ChatGPT plugin was only tested on Windows.

This ChatGPT plugin requires 
* Python 3.x
   * flask-cors
   * swiplserver

Python can be installed from https://www.python.org/downloads/  

Once Python is installed  
> pip install flask-cors  
> pip install swiplserver  

---

To start HTTP server:

Open command prompt
Change to directory containing `main.py`  
`> python main.py`

Example of HTTP server starting.

C:\Users\Groot\SWI-Prolog REPL>python main.py
 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5003
 * Running on http://192.168.1.143:5003
Press CTRL+C to quit

---

To use plugin you will need ChatGPT plugin developer option `Develop your own plugin`

If you do not have the option then you can not use this ChatGPT plugin. At present there are no plans to install into the ChatGPT plugin store.



