# simple way
$my_arr = 25, "Codecademy", 1, $False

$my_arr

# using subexpression operator @

$arr_1 = @($True, 5, (Get-Date).DateTime) # 3 elements
$arr_2 = @( )                             # Empty Array
$arr_3 = @(                               # Multi-line Array
    "Uno"
    "Dos"
    "Tres"
) 

$arr_1
$arr_2
$arr_3

# Indexing

$food = "pizza", "burrito", "curry", "pho", "fries", "soup"


$favorite = $food[3]
$food[2] = "samosa"
$fast_food = $food[0, 1, 4]
$reverse_food = $food[5..0]
$fast_food.ForEach({ "Fast foods: " + $PSItem })

# Testing
Write-Host My favorite food is $favorite
Write-Host The foods in reverse:
$reverse_food

# Length method
$car_types = "suv", "sedan", "pickup", "convertible"
$car_types.ForEach({ $_.Length })