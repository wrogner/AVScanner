<img src="doc/img/AVScanner.png" width="150">

# AVScanner

A ClamAV frontend to scan for Viruses

### Requirements

- [ClamAV](https://www.clamav.net/) installed locally on the machine (and accessible on the $PATH)</br>
  (on Mac, install via [brew](https://formulae.brew.sh/formula/clamav#default))
- [CustomTkinter](https://customtkinter.tomschimansky.com/documentation/widgets) (by Tom Schimansky)
- [Pillow](https://pillow.readthedocs.io/en/stable/reference/Image.html)

<br>

Code Repo: https://github.com/wrogner/AVScanner

### Credits

&copy; 2023 by war

### Open Issues / Roadmap

<img src="doc/img/roadmap.png" width="100">

TODO:<br>
<sub>(Note: I use [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) in VSCode to color-codes stati. It's optional and not transfered to the markdown file.)</sub>

[x] Add remote repo<br>
[x] Setup GUI editing<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PyGubu not really usable (outdated code)<br>
[x] Create application framework<br>
[x] Application deployment (packaging, executable)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[x] create PyPI account [https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[x] install build tools (build, setuptools) [https://setuptools.pypa.io/en/latest/index.html]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[x] create buildable package [https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[x] upload using twine [https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives]<br>
[ ] Update logic<br>
[ ] Simple Scanning (single file / directory)<br>
[ ] update database (call freshclam)<br>

