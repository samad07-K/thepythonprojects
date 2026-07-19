Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=== RESTART: C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py ===
Traceback (most recent call last):
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py", line 2, in <module>
    from PIL import Image,ImageTk
ModuleNotFoundError: No module named 'PIL'

=== RESTART: C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py ===
Traceback (most recent call last):
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py", line 2, in <module>
    from PIL import Image,ImageTk
ModuleNotFoundError: No module named 'PIL'

=== RESTART: C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py ===
Traceback (most recent call last):
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py", line 2, in <module>
    from pil import Image,ImageTk
ModuleNotFoundError: No module named 'pil'

=== RESTART: C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py ===
Traceback (most recent call last):
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py", line 2, in <module>
    from pil import Image,ImageTk
ModuleNotFoundError: No module named 'pil'

=== RESTART: C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py ===
Traceback (most recent call last):
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py", line 14, in <module>
    images=[Image.open(path).resize(image_size) for path in inamge_paths]
NameError: name 'inamge_paths' is not defined. Did you mean: 'image_paths'?

=== RESTART: C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py ===
Traceback (most recent call last):
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py", line 14, in <module>
    images=[Image.open(path).resize(image_size) for path in image_paths]
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\Lib\site-packages\PIL\Image.py", line 3639, in open
    fp = builtins.open(filename, "rb")
PermissionError: [Errno 13] Permission denied: 'C:\\Users\\SAMAD\\OneDrive\\Pictures'

=== RESTART: C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py ===
Traceback (most recent call last):
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py", line 19, in <module>
    images=[Image.open(path).resize(image_size) for path in image_paths]
NameError: name 'image_paths' is not defined. Did you mean: 'image_files'?

=== RESTART: C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py ===
Traceback (most recent call last):
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py", line 21, in <module>
    label=tk.label(pack)
AttributeError: module 'tkinter' has no attribute 'label'. Did you mean: 'Label'?

=== RESTART: C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py ===
Traceback (most recent call last):
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py", line 21, in <module>
    label=tk.Label(pack)
NameError: name 'pack' is not defined
>>> 
=== RESTART: C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py ===
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\Lib\tkinter\__init__.py", line 1948, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py", line 31, in start_slideshow
    update_image()
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py", line 25, in update_image
    label.config(image=photo_image)
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\Lib\tkinter\__init__.py", line 1702, in configure
    return self._configure('configure', cnf, kw)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\Lib\tkinter\__init__.py", line 1692, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: invalid command name ".!label"
>>> 
=== RESTART: C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py ===
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\Lib\tkinter\__init__.py", line 1948, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py", line 31, in start_slideshow
    update_image()
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\slideshow app.py", line 25, in update_image
    label.config(image=photo_image)
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\Lib\tkinter\__init__.py", line 1702, in configure
    return self._configure('configure', cnf, kw)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\SAMAD\AppData\Local\Programs\Python\Python312\Lib\tkinter\__init__.py", line 1692, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: invalid command name ".!label"
