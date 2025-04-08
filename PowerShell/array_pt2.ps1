$dogs_arr = @(
    [PSCustomObject]@{Name = 'Rufus'; Age = 10}
    [PSCustomObject]@{Name = 'Miku'; Age = 2}
)

$dogs_arr.ForEach({ $_.Name + " is " + $_.Age + " years old."})

$spanish_nums_1 = "Uno", "Dos", "Tres"
$spanish_nums_2 = "Cuatro", "Cinco"

# Make changes below
$spanish_nums = $spanish_nums_1 + $spanish_nums_2 
$is_seis_in_spanish_nums = $spanish_nums -contains 'seis'
[Int[]]$nums = 1, 2, 3, 4, 5
$spanish_nums_join_string = $spanish_nums -join ", "
$nums_join_string = $nums -join " >> "
# Make changes above

Write-Host `nNumbers are: $nums_join_string
Write-Host Spanish numbers are: $spanish_nums_join_string
Write-Host Is seis in spanish_nums? $is_seis_in_spanish_nums