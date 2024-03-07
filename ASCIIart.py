# pip install pywhatkit
# pip install ascii-magic

import pywhatkit as kit
import ascii_magic
# kit.image_to_ascii_art("C:/Users/OneDrive/Desktop/PP/house.jpg", "houseee.txt")
output = ascii_magic.from_image_file("C:/Users/OneDrive/Desktop/PP/house.jpg",
                                     columns=300, char="*")
ascii_magic.to_terminal(output)