$person = New-Object -TypeName PSCustomObject

$person | Add-Member -MemberType NoteProperty -Name "FirstName" -Value "Nick"

$person | Add-Member -MemberType ScriptMethod -Name "greeting" -Value {Write-Host "Hello there!"}

# $person.greeting()

# Using hashtables 

$person = [PSCustomObject]@{
    Name = "Nick"
    Age = 24
}

$person | Get-Member -MemberType NoteProperty