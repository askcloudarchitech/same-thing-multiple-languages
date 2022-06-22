<?php

// To use
// Install PHP : https://www.php.net/manual/en/install.php
// after install, navigate to this dir in your terminal and run
// php -f thing.php

class Thing{
   public function __construct(
    private $color,
    private $shape,
   ){}

   public function printColor(){
    echo $this->color . "\n";
   }

   public function getColor(){
    return $this->color;
   }

   public function printShape(){
    echo $this->shape  . "\n";
   }

   public function isItRed(){
    if ($this->color == "red") {
        return true;
    }
    return false;
   }

}

function redBlueCounts($things) {
    $redcount = 0;
    $bluecount = 0;
    foreach ($things as $thing) {
        switch ($thing->getColor()) {
            case "red" :
                $redcount++;
                break;
            case "blue" :
                $bluecount++;
                break;
        }
    }
    echo "blue: ". $bluecount . "\nred: " . $redcount . "\n";
}


$things[0] =  new Thing("red", "square");
$things[1] =  new Thing("blue", "round");
$things[2] =  new Thing("red", "round");

foreach ($things as $thing) {
    $thing->printColor();

    if ($thing->isItRed()) {
        echo "it's red\n";
    } else {
        echo "it's not red\n";
    }
}

redBlueCounts($things);



