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

def style_button():
  button = document.getElementById("madeFrompython")
  button.setAttribute("type", "button")
  button.style.backgroundColor = "#306998"
  button.style.color = "white"
  button.style.padding = "1rem 2rem"
  button.style.borderRadius = "8px"
  button.style.border = "none"
  button.style.fontWeight = "bold"
  button.style.boxShadow = "0 4px 10px rgba(0, 0, 0, 0.2)"
  button.innerText = "Styled with Python 🐍"
  button.style.marginTop = "1rem"
  button.style.marginBottom = "1rem"
style_button()




#note to self

coding_fieldset = document.getElementById("coding").parentElement

wrapper = document.createElement("div")
wrapper.style.marginTop = "2rem"
wrapper.style.display = "flex"
wrapper.style.flexDirection = "column"
wrapper.style.alignItems = "center"
wrapper.style.gap = "1rem"

# Create the input
url_input = document.createElement("input")
url_input.placeholder = "Enter a long URL to shorten..."
url_input.style.width = "80%"
url_input.style.padding = "1rem"
url_input.style.border = "1px solid #ccc"
url_input.style.borderRadius = "8px"
url_input.style.fontSize = "16px"

# Create the result area
result = document.createElement("p")
result.innerText = "Shortened URL will appear here."
result.style.fontSize = "18px"
result.style.fontWeight = "bold"

# Function to generate a fake shortened URL
def shorten_url(event=None):
    long_url = url_input.value.strip()
    if not long_url:
        result.innerText = "❌ Please enter a valid URL."
        return

    # Create a random 6-character code
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    short_url = f"https://aidn.ly/{code}"
    result.innerHTML = f"✅ <a href='{long_url}' target='_blank'>{short_url}</a>"

# Create the button
shorten_btn = document.createElement("button")
shorten_btn.setAttribute("type", "button")
shorten_btn.innerText = "Shorten URL"
shorten_btn.style.padding = "0.75rem 1.5rem"
shorten_btn.style.backgroundColor = "#306998"
shorten_btn.style.color = "white"
shorten_btn.style.border = "none"
shorten_btn.style.borderRadius = "8px"
shorten_btn.style.fontWeight = "bold"
shorten_btn.onclick = shorten_url

# Append everything to wrapper and insert
wrapper.appendChild(url_input)
wrapper.appendChild(shorten_btn)
wrapper.appendChild(result)
coding_fieldset.appendChild(wrapper)
