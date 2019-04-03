package engine

import "crawler/engine"

type Request struct {
	Url        string
	ParserFunc func([]byte) engine.ParserResult
}

type ParseResult struct {
	Requests []Request
	Items    []interface{}
}

func NilParser([]byte) ParseResult {
	return ParseResult{}
}
