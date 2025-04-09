# using else/elseif
$var = 4
if ($var -gt 10) { 
	Write-Host "Larger than 10"
} elseif ($var -gt 5) {
  Write-Host "Larger than 5"
} elseif ($var -gt 0) {
  Write-Host "Larger than 0"
} else {
  Write-Host "Nothing!"
}

# using switch
# checks all conditions even if one is true
$var = 5
switch ($var) {
  5 { 
    Write-Host "Equal to 5!"
  }
  {$_ -lt 0} {
    Write-Host "Less than 0."
  }
  {$_ -gt 0} {
    Write-Host "Greater than 0."
  }
  default {
    Write-Host "Something..."
  }
}
