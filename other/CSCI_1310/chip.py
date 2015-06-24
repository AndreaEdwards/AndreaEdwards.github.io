#!opt/local/bin/python2.7

pmol = 1 * (10 ** (-12))
bp_mw = 300
length = 200
oligo_wt = bp_mw * pmol * 0.00001 * length
print "oligo weight is ", oligo_wt
chip = oligo_wt * 55000
print "chip weight is ", chip
