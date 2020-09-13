;
; AutoIt Version: 3.0
; Language:       Spanish
; Platform:       x64
; Author:         Oleksis Fraga <oleksis.fraga@gmail.com>
;
; AutoIt can be downloaded from:
;   https://www.autoitscript.com/site/autoit/
;
; Use-case:
; 1. Selenium run some browser test (default Chrome)
; 2. The test requires save file
; 3. Selenium press 'Print..' button which calls 'Print' dialog
; 4. It is operation system's dialog and can not be controled via Selenium
;    (JavaScript)
; 5. Selenium test run compiled version of this script (script.exe). This
;    script specifies file and closes the dialog
; 6. Selenium test contunies
;
; Run:
;   handle_save_as.exe chrome "path/to/file/file.pdf"
;


#include <MsgBoxConstants.au3>

If $CmdLine[1] == "chrome" Then
    $sTitle = "Guardar como"
Else
    MsgBox($MB_SYSTEMMODAL, "", "Unknown browser")
    Exit
EndIf

; Find window
WinActivate($sTitle)

; Path to the file
send($CmdLine[2])
Sleep(2000)

; Save and continuing
;Send("{ENTER}")

; Now quit by sending a "close" request to the calculator window using the classname
;WinClose($sTitle)

; Now wait for the calculator to close before continuing
;WinWaitClose($sTitle)
