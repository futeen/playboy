package main

import "fmt"

// character and ascii

func main() {
	// character to ascii
	char := 'a' // rune, not string
	ascii := int(char)
	fmt.Println(string(char), ":", ascii)

	// ascii to character
	asciiNum := 65
	character := string(asciiNum)
	fmt.Println(asciiNum, ":", character)
}
