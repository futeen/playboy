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
	b, err := strconv.ParseInt(a, 10, 32)

	if err != nil {
		panic(err)
	}
	result := int32(b)
	fmt.Printf("%T", result)
}