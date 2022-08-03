// Javascript
// Node is useful to have

class Thing {
  constructor(color, shape) {
    this.color = color;
    this.shape = shape;
  }
  setColor(color) {
    this.color = color;
  }
  setShape(color) {
    this.color = color;
  }
  getColor() {
    return this.color;
  }
  getShape() {
    return this.shape;
  }
  printColor() {
    console.log(this.color);
  }
  printShape() {
    console.log(this.shape);
  }
  isItRed() {
    if (this.color.toLowerCase() === "red") {
      return true;
    } else {
    return false;
  }
  }
}

/**
 * @param {array} things
 */
function redBlueCounts(things) {
  let redCount = 0;
  let blueCount = 0;

  for (let i = 0; i < things.length; i++) {
    thing = things[i]
    if (thing.getColor().toLowerCase() === "red") {
      redCount++;
    } else if (thing.getColor().toLowerCase() === "blue") {
      blueCount++;
    }
  }
  console.log("blue: ", blueCount, "red: ", redCount);
}

// main part of file
things = [];
things.push(new Thing("red", "square"));
things.push(new Thing("blue", "round"));
things.push(new Thing("red", "round"));

for (let i = 0; i < things.length; i++) {
  thing = things[i];
  thing.printColor();
  if (thing.isItRed() === true) {
    console.log("it's red");
  } else {
    console.log("it's not red")
  }
  
}
redBlueCounts(things)
