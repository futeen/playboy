package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Scan()
	a := input.Text()
	b, err := strconv.Atoi(a)

	if err != nil {
		panic(err)
	}

	fmt.Printf("%T", b)
}