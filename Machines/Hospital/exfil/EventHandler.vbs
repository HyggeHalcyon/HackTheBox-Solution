'   Sub OnClientConnect(oClient)
'   End Sub

'   Sub OnSMTPData(oClient, oMessage)
'   End Sub

'   Sub OnAcceptMessage(oClient, oMessage)
'   End Sub

'   Sub OnDeliveryStart(oMessage)
'   End Sub

'   Sub OnDeliverMessage(oMessage)
'   End Sub

'   Sub OnBackupFailed(sReason)
'   End Sub

'   Sub OnBackupCompleted()
'   End Sub

'   Sub OnError(iSeverity, iCode, sSource, sDescription)
'   End Sub

'   Sub OnDeliveryFailed(oMessage, sRecipient, sErrorMessage)
'   End Sub

'   Sub OnExternalAccountDownload(oFetchAccount, oMessage, sRemoteUID)
'   End Sub

Function RunCommand(sCommand)
	Dim obShell
	Set obShell = CreateObject("WScript.Shell")
	obShell.Run sCommand, 0, true
	Set obShell = Nothing
End Function

Sub SaveAttachment(oMessage)
	Dim i, strDir, strFile
	strDir = "C:\Users\drbrown.HOSPITAL\Downloads\"
	For i = 0 To oMessage.Attachments.Count-1
		strFile = oMessage.Attachments.item(i).Filename
		oMessage.Attachments.item(i).SaveAs(strDir & strFile)
	Next
	If Right(strFile, 4) = ".eps" Then
        	call RunCommand("C:\Users\drbrown.HOSPITAL\Documents\ghostscript.bat " & strFile)
	Else
		Dim fso, file
		Set fso = CreateObject("Scripting.FileSystemObject")
		fso.DeleteFile strDir & strFile
	End If

End Sub