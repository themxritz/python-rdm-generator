import os

strLicense = """

## [License](#license)

```text
The MIT License (MIT)
Copyright (c) 2022 Moritz Selz
 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


"""
with open('README.md', 'a') as file:
    name = input("Projectname » ")
    file.write("## [ " + name + "](#name)")
    file.write("\n[![License](https://img.shields.io/github/license/vhesener/Closures.svg?style=plastic&colorB=68B7EB)]()\n\n")

    description = input("description » ")
    file.write(description)

    file.write("## [Setup](#usage-overview)\n")
    Setupdescription = input ("Setup description » ") 
    file.write(Setupdescription)

    Setupcommand = input("Setup command » ")
    file.write("```swift\n + " + Setupcommand +  "\n ```")
    file.write(strLicense)

