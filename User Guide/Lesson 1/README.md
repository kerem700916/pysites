# LESSON 1
# creating a basic web page
input
```python
import pysites
from pysites import load_basic
from pysites import open_in_browser
web_page = load_basic()
path = '/home/pi/index.html'
open_in_browser(path)
```
<a href="assets/ss1.png">Output</a>
<img src="assets/ss1.png">

# As you see you created a basic website, now let me explain the code
```python
import pysites # importing the library
```
```python
from pysites import load_basic # also import the loab_basic function to create a basic website
```
```python
from pysites import open_in_browser # and also this to open in your browser
```
```python
web_page = load_basic() # code to load the basic website
```
```python
path = '/home/pi/index.html' # this part is important. Get the directory that you saved the library after, you will see the "index.html" file. Copy the path. And paste it
```
```python
open_in_browser(path) # and finally opening on the browser
```
# Done! Lesson 1 is over
<hr>
