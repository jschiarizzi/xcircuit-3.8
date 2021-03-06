# XCircuit Python startup script (xcstartup.py)
# Does the work previously handled by "builtins.lps".  Commands
# "loadlibrary" and "loadfontencoding" should no longer be used.
#
#  Written by Tim Edwards 1/19/01 (tim@bach.ece.jhu.edu)
#  The Johns Hopkins University

font("times_roman.xfe")
font("times_romaniso.xfe")
font("helvetica.xfe")
font("helveticaiso.xfe")
font("courier.xfe")
font("courieriso.xfe")
font("symbol.xfe")

# Alternate font encodings:  Uncomment these if you want them
# loaded by default
#
# font("times_romaniso2.xfe")
# font("courieriso2.xfe")
# font("helveticaiso2.xfe")
# font("times_romaniso5.xfe")
# font("courieriso5.xfe")
# font("helveticaiso5.xfe")

# First library page
library("generic.lps", 1)
library("analog.lps", 1)
library("avlsi.lps", 1)
library("digital.lps", 1)

# Second library page
library ("analoglib2.lps", 2)

# Third library page
library ("ic_templates.lps", 3)

# Fourth library page
library ("quadparts.lps", 4)

