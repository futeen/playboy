package main

import (
	"bufio"
	"fmt"
	"os"
	"pra_demo"
	"strconv"
)
// 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

func queued(n string) []int32 {
	var list []int32
	for _, i := range n {
		list = append(list, i)
	}
	pra_demo.QSortRecursion(list)
	return list
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Scan()
	a := input.Text()
	b, err := strconv.ParseInt(a, 10, 32)

	if err != nil {
		panic(err)
	}
	result := int32(b)
	convert := int64(result)

	last := strconv.FormatInt(convert, 10)
	fmt.Printf("%T", last)

	arr := queued(last)
	fmt.Println(arr)
	finalNum := ""
	for _, i := range arr {
		finalNum = finalNum + string(i)
	}
	fmt.Println(finalNum)

}
