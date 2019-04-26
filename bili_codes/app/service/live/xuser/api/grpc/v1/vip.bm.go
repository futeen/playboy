// Code generated by protoc-gen-bm v0.1, DO NOT EDIT.
// source: api/grpc/v1/vip.proto

/*
Package v1 is a generated blademaster stub package.
This code was generated with go-common/app/tool/bmgen/protoc-gen-bm v0.1.

It is generated from these files:
	api/grpc/v1/vip.proto
*/
package v1

import (
	"context"

	bm "go-common/library/net/http/blademaster"
	"go-common/library/net/http/blademaster/binding"
)

// to suppressed 'imported but not used warning'
var _ *bm.Context
var _ context.Context
var _ binding.StructValidator

// =============
// Vip Interface
// =============

type Vip interface {
	// Info 返回用户vip信息
	Info(ctx context.Context, req *UidReq) (resp *InfoReply, err error)

	// Buy 购买月费/年费姥爷
	Buy(ctx context.Context, req *BuyReq) (resp *BuyReply, err error)
}

var v1VipSvc Vip

// @params UidReq
// @router GET /xlive/xuser/v1/vip/Info
// @response InfoReply
func vipInfo(c *bm.Context) {
	p := new(UidReq)
	if err := c.BindWith(p, binding.Default(c.Request.Method, c.Request.Header.Get("Content-Type"))); err != nil {
		return
	}
	resp, err := v1VipSvc.Info(c, p)
	c.JSON(resp, err)
}

// @params BuyReq
// @router GET /xlive/xuser/v1/vip/Buy
// @response BuyReply
func vipBuy(c *bm.Context) {
	p := new(BuyReq)
	if err := c.BindWith(p, binding.Default(c.Request.Method, c.Request.Header.Get("Content-Type"))); err != nil {
		return
	}
	resp, err := v1VipSvc.Buy(c, p)
	c.JSON(resp, err)
}

// RegisterV1VipService Register the blademaster route with middleware map
// midMap is the middleware map, the key is defined in proto
func RegisterV1VipService(e *bm.Engine, svc Vip, midMap map[string]bm.HandlerFunc) {
	v1VipSvc = svc
	e.GET("/xlive/xuser/v1/vip/Info", vipInfo)
	e.GET("/xlive/xuser/v1/vip/Buy", vipBuy)
}
