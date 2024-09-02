<?php
$numbers = [1, 2, 3, 4, 5];
$sum = 0;
$i = 0;

while ($i < count($numbers)) {
    $sum += $numbers[$i];
    $i++;
}

echo "Sum using while loop: $sum\n";
?>
