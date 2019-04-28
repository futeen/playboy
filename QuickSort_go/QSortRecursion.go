package main

import (
	"fmt"
	"math/rand"
	"time"
)

//��·����
/*
�ݹ�汾ʵ��

����ͨ�������ѡȡ�Ƚϵĵ�
���� head + 1-> tail
����mid ���tail���� ����tail�C
С�ڵ��� �򽻻�head ����head++ i++
���ʣ�

Ϊʲô�ڴ��ڵ������ index i û����λ��
��Ϊ�������tail����û�б�֤һ�������midԪ�أ�������Ҫ�ٴν��бȽ�

Ϊʲô��С�ڵ������ index i ��Ҫ��λ��
��Ϊ��һ�ν�����ʱ����arr[0] -> mid�����Խ�����һ������arr[i] <= mid�����Կ�����λ��������������޷�����

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
