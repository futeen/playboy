package main

import (
	"fmt"
	"regexp"
)

const text = `
my email is ccmouse@gmail.com@abc.com
email1 is abc@def.org
email2 is    kkk@qq.com
email3 is ddd@abc.com.cn
`

func main() {
	exam := `<a href="http://www.zhenai.com/zhenghun/chongqing" data-v-5e16505f>重庆</a>"`

	re := regexp.MustCompile(`<a href="(http://www.zhenai.com/zhenghun/[0-9a-z]+)"[^>]*>([^<]+)</a>"`)
	match := re.FindAllStringSubmatch(exam, -1)
	for _, m := range match {
		fmt.Println(m)
	}
}