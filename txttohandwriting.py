#pip install pywhatkit
import pywhatkit as pw

txt = """The main purpose of using triple quotes in python is to create multi-line strings and docstrings. We can create triple quotes using double (“““ ”””) as well as single (''' ''') quotes."""
pw.text_to_handwriting(txt, "demo.png", [0,0,138])
#if you dont use 2nd paramter -> demo.png, it is automatically saved as pywhatkit.png
#default color is blue
print("END")