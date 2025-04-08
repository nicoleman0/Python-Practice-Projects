$person = New-Object -TypeName PSCustomObject

$person | Add-Member -MemberType NoteProperty -Name "FirstName" -Value "Nick"

$person | Add-Member -MemberType ScriptMethod -Name "greeting" -Value {Write-Host "Hello there!"}

$person.greeting()