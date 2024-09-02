<?php
$numbers = [1, 2, 3, 4, 5];
$sum = 0;

for ($i = 0; $i < count($numbers); $i++) {
    $sum += $numbers[$i];
}

echo "Sum using for loop: $sum\n";
?>
