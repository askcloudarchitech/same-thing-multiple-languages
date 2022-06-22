package main

// to use
// install Go: https://go.dev/doc/install
// after install, navigate to this directory in your termainal and run
// go run thing.go

import "fmt"

type Thing struct {
	color string
	shape string
}

var things []Thing

func (t *Thing) SetColor(color string) {
	t.color = color
}

func (t *Thing) SetShape(shape string) {
	t.shape = shape
}

func (t *Thing) GetColor() string {
	return t.color
}

func (t *Thing) PrintColor() {
	fmt.Println(t.color)
}

func (t *Thing) PrintShape() {
	fmt.Println(t.shape)
}

func (t *Thing) IsItRed() bool {
	if t.color == "red" {
		return true
	}
	return false
}

func NewThing(color string, shape string) Thing {
	newthing := Thing{}
	newthing.SetColor(color)
	newthing.SetShape(shape)
	return newthing
}

func RedBlueCounts(things []Thing) {
	redcount := 0
	bluecount := 0

	for _, thing := range things {
		switch thing.GetColor() {
		case "red":
			redcount++
			break
		case "blue":
			bluecount++
			break
		}
	}
	fmt.Printf("blue: %x \nred: %x \n", bluecount, redcount)
}

func main() {
	things = append(things, NewThing("red", "square"))
	things = append(things, NewThing("blue", "round"))
	things = append(things, NewThing("red", "round"))

	for _, thing := range things {
		thing.PrintColor()
		if thing.IsItRed() {
			fmt.Println("it's red")
		} else {
			fmt.Println("it's not red")
		}
	}

	RedBlueCounts(things)

}
