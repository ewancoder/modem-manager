del /s /f /q _build\latex
call make.bat latex
call make.bat latex
cd _build\latex
"c:\Program Files (x86)\MiKTeX 2.9\miktex\bin\pdflatex.exe" ModemManager.tex
"c:\Program Files (x86)\MiKTeX 2.9\miktex\bin\pdflatex.exe" ModemManager.tex
cd ..\..
mkdir Release
copy /Y _build\latex\ModemManager.pdf Release\ModemManager-ru.pdf
