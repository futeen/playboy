package main

import "fmt"

func fibonacci(channel chan int, quit chan bool) {
	x, y := 1, 1
	for {
		select {
		case channel <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("finish")
			return
		}
	}
}

func main() {
	channel := make(chan int)
	quit := make(chan bool)

	go func() {
		for i:=0; i<10; i++ {
			num := <-channel
			fmt.Println("num is ", num)
		}
		quit <- true
	}()
	fibonacci(channel, quit)
}
