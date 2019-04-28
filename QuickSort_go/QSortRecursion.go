package main

import (
	"fmt"
	"math/rand"
	"time"
)

//单路快排
/*
递归版本实现

首先通过随机数选取比较的点
遍历 head + 1-> tail
大于mid 则和tail交换 并且tail–
小于等于 则交换head 并且head++ i++
疑问：

为什么在大于的情况下 index i 没有移位？
因为交换后的tail，并没有保证一定会大于mid元素，所以需要再次进行比较

为什么在小于的情况下 index i 需要移位？
因为第一次交换的时候是arr[0] -> mid，所以交换后一定满足arr[i] <= mid，所以可以移位操作。否则遍历无法结束

*/

func QSortRecursion(arr []int) {
	arrLen := len(arr)
	if arrLen <= 1 {
		return
	}

	randNum := getRandNum(arrLen - 1)
	arr[randNum], arr[0] = arr[0], arr[randNum]
	mid := arr[0]
	head, tail := 0, arrLen - 1

	for i:=1; i<=tail; {
		if arr[i] > mid {
			arr[i], arr[tail] = arr[tail], arr[i]
			tail--
		} else {
			arr[i], arr[head] = arr[head], arr[i]
			head++
			i++
		}
	}
	QSortRecursion(arr[:head])
	QSortRecursion(arr[head+1:])
	fmt.Println("third print: ", arr)
}

func getRandNum(totalNum int) int {
	rand.Seed(time.Now().Unix())
	return rand.Intn(totalNum)
}

func main() {
	arr := []int{3, 4, 5, 6, 7, 1, 2, 9}
	QSortRecursion(arr)
}
