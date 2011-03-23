TexShop pdflatex Command
========================

TexShop is a program for Mac OS X which compiles LaTex files (.tex) into pdf files. When it does this, by default it created a .log and .aux file for every source file in your LaTeX document, this gets annoying with large projects.

It is a simple enough modification to get all output files to appear in a different directory, however **this script moves the generated pdf file back to project directory**. My script builds on one which discovered here:

http://hints.macworld.com/article.php?story=20070906022746216

This repository holds my modified version of this concept, in addition putting the script in a repository prevents me from loosing it later on.

Installing the Script
---------------------

You can put the script anywhere, but the solution I am following suggests, putting it here:

    /Library/TeX/Root/bin/pdflatex.py

Make sure that everyone has executable permissions on the file, if TexShop cannot execute the file it will complain:

    sudo chmod +x /Library/TeX/Root/bin/pdflatex.py

Next change TexShop's preferences to use this script instead, go to **Preferences** and then the **Engine** tab. Under the section entitles **pdfTeX** change the **Latex (default: pdflatex)** box to use the new script.

For example if before it looked like this:

    pdflatex --file-line-error --shell-escape --synctex=1

And afterwards it should look like this:

    /Library/TeX/Root/bin/pdflatex.py --file-line-error --shell-escape --synctex=1

Any arguments passed to the new `pdflatex.py` script will be passed on the real `pdflatex` command which is subsequently called.

Setting the Output Directory
----------------------------

By default all generated files will appear in `/tmp`, you can override this in the standard `pdflatex` command using the `--output-directory=/path/to/location` argument.

All that the new pdflatex.py script does is call the original `pdflatex` command and then move the pdf file back to the directory which the root .tex file is in.

As an example, if you wanted to have all of the output files put into a `build` directory next to the root text file, the just add `--output-directory=build` to argument list in the TexShop preferences for pdflatex.py command.