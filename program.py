from js import document
import random, string

#BASIC HELPER FUNCTIONS
def add_text(text, size=18):
  #Adds a paragraph of text to the body of the page.
  #
  #Parameters:
  #    - text (str): The text to add.
  #    - size (int, optional): Font size in pixels. Defaults to 18.
  #
  #Returns:
  #    - The created <p> element.
  element = document.createElement("p")
  text = str(text)
  element.innerHTML = text.replace("\n", "<br />").replace("\\n", "<br />")
  element.style.fontSize = f"{size}px"
  document.body.appendChild(element)
  return element

def add_button(label, size=18, on_click=None):
  #Adds a button to the body of the page.
  #
  #Parameters:
  #    - label (str): The text displayed on the button.
  #    - size (int, optional): Font size in pixels. Defaults to 18.
  #    - on_click (function, optional): A Python function to call when the button is clicked.
  #
  #Returns:
  #    - The created <button> element.
  button = document.createElement("button")
  button.textContent = str(label)
  button.style.fontSize = f"{size}px"
  button.style.padding = "0.5rem 1rem"
  button.style.margin = "0.5rem"
  button.style.cursor = "pointer"

  # If a click handler function is provided, add it
  if on_click:
      def js_callback(e):
          on_click()
      button.addEventListener("click", js_callback)

  document.body.appendChild(button)
  return button

def clear_canvas(preserve_height=True):
#  Clears all content inside the element with ID 'canvas',
#  but preserves the layout space so things don't shift.

#  Parameters:
#      - preserve_height (bool): If True, replaces contents with invisible spacers.
#
#  Example:
#      clear_canvas()  # clears content, keeps layout
  canvas = document.getElementById("canvas")

  if canvas:
      # Get current height (optional)
      height = canvas.offsetHeight

      # Remove all children
      while canvas.firstChild:
          canvas.removeChild(canvas.firstChild)

      if preserve_height:
          # Add a transparent spacer div to keep the space
          spacer = document.createElement("div")
          spacer.style.height = f"{height}px"
          spacer.style.opacity = "0"
          spacer.style.pointerEvents = "none"
          canvas.appendChild(spacer)
  else:
      print("⚠️ No element with ID 'canvas' found.")

def position_element(element, x, y):
  #Positions the given `element` on the page using x and y values.
  #
  #Parameters:
  #    - element (element): The DOM element to position.
  #    - x (int|str): Horizontal position ("left", "center", "right" or number of pixels).
  #    - y (int|str): Vertical position ("top", "center", "bottom" or number of pixels).
  element.style.position = "absolute"

  get_flex_align = {
      "center": "center",
      "right": "flex-end",
      "left": "flex-start",
  }

  # Handle x position
  if isinstance(x, str):
      element.style.alignSelf = get_flex_align[x]
  else:
      element.style.left = str(x) + "px"

  # Handle y position
  if isinstance(y, str):
      if y == "bottom":
          if element.tagName == "IMG":
              element.onload = lambda _: _set_y_to_bottom(element)
          else:
              _set_y_to_bottom(element)
      elif y == "top":
          if element.tagName == "IMG":
              element.onload = lambda _: _set_y_to_top(element)
          else:
              _set_y_to_top(element)
      elif y == "center":
          if element.tagName == "IMG":
              element.onload = lambda _: _set_y_to_center(element)
          else:
              _set_y_to_center(element)
  else:
      element.style.top = str(y) + "px"
#HELPER FUNCTIONS END

#Styles for the "Styled with Python button" in HTML, id = "made_from_python"
def style_button():
  #Get the button's id
  button = document.getElementById("madeFrompython")
  #Change the text inside
  button.innerText = "Styled with Python 🐍"
  #Styles
  button.setAttribute("type", "button")
  button.style.backgroundColor = "#306998"
  button.style.color = "white"
  button.style.padding = "1rem 2rem"
  button.style.borderRadius = "8px"
  button.style.border = "none"
  button.style.fontWeight = "bold"
  button.style.boxShadow = "0 4px 10px rgba(0, 0, 0, 0.2)"
  button.style.marginTop = "1rem"
  button.style.marginBottom = "1rem"
  button.style.cursor = "pointer"
style_button()
