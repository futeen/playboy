func getRandNum(totalNum int) int {
	rand.Seed(time.Now().Unix()) // rand.Seed() 的参数发生变化，会产生不同的随机数
	return rand.Intn(totalNum)