import glob
  # directory that holds files
print "All txt files in the directory are being concatenated to :"
print" ----------------------------------------------------------"
print " TMNTIBA.LPSSORZZ.CTLLIB00.CPARSE.XMLMOD2(AAAAAAA)"
print" ----------------------------------------------------------"
#filename = raw_input("ENTER FILENAME TO BE CREATED(INCLUDE EXTENSION; TXT CSV XML .. ETC: \n ->")

read_files2 = glob.glob("*.txt")
print read_files2
with open("out.prn", "wb") as outfile:
    for f in read_files2:
        with open(f, "rb") as infile:
             outfile.write(infile.read())
print "finished"
