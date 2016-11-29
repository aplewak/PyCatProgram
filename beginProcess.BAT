
@echo off
echo open hostname>> u.ftp
echo username>> u.ftp
echo password>> u.ftp
echo cd ..>> u.ftp
echo cd " directory to be ftpd to ">> u.ftp
echo PUT C:path that contains the outfile AAAAAAA>> u.ftp
echo disconnect>> u.ftp
echo quit>> u.ftp
call sendtomf.bat