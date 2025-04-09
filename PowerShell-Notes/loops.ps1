# for loop
for ($i = 1; $i -le 10; $i++) {
    $square = $i*$i
    Write-Host "i is ($i)"
    Write-Host "The square of ($i) is ($square)."
  }


# for each
$recipe = "flour", "sugar", "salt", "oil"
foreach ($ingredient in $recipe) {
  Write-Host "My recipe includes" $ingredient
}

# while 
$count = 0

while ($count -le 30) {
  $count+=3
  Write-Host $count
}

# Do / Until
$position = 10
$goal = 0

do {
  $position -= 1
  Write-Host $position "and" $goal
} until ($position -eq $goal)

# Break
$count = 0
while ($count -lt 5) {
  $count++
  if ($count -eq 3) {
    break
  }
  Write-Host "While loop:" $count
}

# Continue
for ($i = 0; $i -lt 10; $i++) {
    if ($i % 2 -eq 0) {
      continue
    }
    Write-Host "For loop:" $i
  }

