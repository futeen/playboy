func getRandNum(totalNum int) int {
	rand.Seed(time.Now().Unix()) // rand.Seed() �Ĳ��������仯���������ͬ�������
	return rand.Intn(totalNum)