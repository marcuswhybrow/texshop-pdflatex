#!/usr/bin/python

import os, sys, shutil

OUTPUT_ARGUMENT = '--output-directory='
DEFAULT_OUTPUT_PATH = '/tmp'

# Grab the output directory from the arguments
output_arg_specified = False
output_dir = None
for arg in sys.argv:
    if arg.startswith(OUTPUT_ARGUMENT):
        output_arg_specified = True
        output_dir = arg.split('=')[1]
        break

# If an output directory argument was not found, then set it to the default
if output_dir is None:
    output_dir = DEFAULT_OUTPUT_PATH

# The output pdf will be named the same as the tex file
tex_file = sys.argv[-1]
pdf_file_name, extention = os.path.splitext(tex_file)

# Not sure why this is necessary
assert extention == '.tex'

if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

# If command arguments did not contain the oput directory argument, then since
# we set it to have a new detault, add it to the arguments we will pass on
args = sys.argv[1:]
if not output_arg_specified:
    args.insert(0, OUTPUT_ARGUMENT + output_dir)

command = 'pdflatex %s' % ' '.join(args)

print '%s Executing: %s' % (sys.argv[0], command)

# Run the original command which generates all the files
os.system(command)

pdf_file_src = '%s%s%s.pdf' % (output_dir, os.path.sep, pdf_file_name)
pdf_file_dest = '%s%s%s.pdf' % (os.curdir, os.path.sep, pdf_file_name)

# If the destination pdf already exists, delete it so that the new one may be
# coppied.
if os.path.isfile(pdf_file_dest):
    os.remove(pdf_file_dest)

# Move the pdf back to where it normally is
shutil.move(pdf_file_src, os.curdir)