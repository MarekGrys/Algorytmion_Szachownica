@echo off
:start
cls
echo Marek Grys
timeout 0 > NUL 
echo Projekt z przedmiotu Jezyki Skryptowe
timeout 0 > NUL 
echo ____________________________________________________________________
timeout 0 > NUL 
echo  ####  #####   ##    ####  #   #  ###  #     # #    # #  ####   ##
timeout 0 > NUL 
echo #         #   #  #  #      #   # #   # #     # ##   #   #      #  #
timeout 0 > NUL 
echo  ####    #   #    # #      #   # #   # #     # # #  # # #     #    #
timeout 0 > NUL 
echo      #  #    ###### #      ##### #   # #  #  # #  # # # #     ######
timeout 0 > NUL 
echo #    # #     #    # #      #   # #   # # # # # #   ## # #     #    #
timeout 0 > NUL 
echo  ####  ##### #    #  ####  #   #  ###   #   #  #    # #  #### #    #
timeout 0 > NUL 
echo ____________________________________________________________________
echo.
echo.
echo.
echo Wybierz opcje z nizej podanych:
timeout 0 > NUL 
echo.
echo 1. Uruchom skrypt python dla plikow w folderze "in"
timeout 0 > NUL 
echo 2. Wyswietl na ekranie informacje o projekcie
timeout 0 > NUL 
echo 3.Utworz kopie zapasowe raportow 
echo 4. Wyjdz z programu
timeout 0 > NUL 
echo.
set /p opcja=wybierz: 
if %opcja%==1 goto 1
if %opcja%==2 goto 2
if %opcja%==3 goto 3
if %opcja%==4 exit
goto blad
:1
cls
echo Uruchamianie skryptu main dla plikow wejsciowych
timeout 0 > NUL 
cls
echo Uruchamianie skryptu main dla plikow wejsciowych.
timeout 1 > NUL
cls
echo Uruchamianie skryptu main dla plikow wejsciowych..
timeout 1 > NUL 
cls
echo Uruchamianie skryptu main dla plikow wejsciowych...
timeout 1 > NUL
cls 
echo _________________________________________________
if not exist out mkdir out
for /f %%f in ('dir /b in') do ( 
   python main.py < in\%%f > out\%%f
   echo Wczytywanie pliku nr %%f
   timeout 0 > NUL
)
del przyklad.txt
echo.
echo Czy chcesz wygenerowac raport? [T/N]
set /p wybor=wybierz: 
if %wybor%==T goto raport
if %wybor%==N goto nie
goto blad
:raport
cls
echo Generowanie raportu
timeout 1 > NUL
cls 
echo Generowanie raportu.
timeout 1 > NUL
cls
echo Generowanie raportu..
timeout 1 > NUL 
cls
echo Generowanie raportu...
timeout 1 > NUL
echo.
echo Wygenerowano raport o nazwie:
python Raport_html.py
echo.
pause
goto start
:nie
pause
goto start
:2
cls
echo Informacje o projekcie:
timeout 0 > NUL 
echo ___________________________________________________________________________
timeout 0 > NUL 
echo Skrypt wyswietla wszystkie mozliwe ruchy bierki zadanej w pliku wejsciowym.
timeout 0 > NUL 
echo Wyniki programu zapisywane sa do pliku wyjsciowego, wyswietlanego pozniej w raporcie html.
timeout 0 > NUL 
echo.
echo Marek Grys (c) 2023
timeout 0 > NUL 
echo Informatyka, semestr III
timeout 0 > NUL 
echo Wydzial Matematyki Stosowanej
pause
goto start
:3
cls
echo Wykonywanie kopii zapasowej raportu
echo __________________________________________
if not exist backup_%date% mkdir backup_%date%
forfiles /M raport*.html  /C "cmd /c copy @file backup_%date%"
echo Wykonano kopie zapasowa wszystkich raportow do folderu backup_%date%
pause
goto start
:blad
echo Bledna opcja, wracanie na start!
pause
goto start