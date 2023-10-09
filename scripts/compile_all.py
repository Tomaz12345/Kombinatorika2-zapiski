import subprocess, sys
import os

# without extension
tex_file = sys.argv[1]

commands = [
    ['pdflatex', '../main/' + tex_file + '.tex', '-output-directory', '../main'],
    ['bibtex', '../main/' + tex_file + '.aux'],
    ['pdflatex', '../main/' + tex_file + '.tex', '-output-directory', '../main'],
    ['pdflatex', '../main/' + tex_file + '.tex', '-output-directory', '../main'],
]

for c in commands:
    print(80 * "*")
    subprocess.call(c)