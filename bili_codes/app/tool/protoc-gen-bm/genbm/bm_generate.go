package genbm

import (
	"fmt"
	"io"

	"go-common/app/tool/protoc-gen-bm/util"
)

const (
	bmPkgPath = "go-common/library/net/http/blademaster"
)

// BMGenerate generate bm server code
type BMGenerate struct {
	target      io.Writer
	packageName string
	descs       []*BMServerDescriptor
	err         error
	jsonpb      bool
}

// NewBMGenerate BMGenerate
func NewBMGenerate(packageName string, descs []*BMServerDescriptor, jsonpb bool) *BMGenerate {
	return &BMGenerate{
		packageName: packageName,
		descs:       descs,
		jsonpb:      jsonpb,
	}
}

// Generate code
func (b *BMGenerate) Generate(target io.Writer) error {
	b.target = target
	methodsCount := 0
	for _, desc := range b.descs {
		methodsCount += len(desc.Methods)
	}
	// if not methods found, can't generate anything
	if methodsCount == 0 {
		return nil
	}
	b.generatePackageImport()
	for _, desc := range b.descs {
		b.generateServer(desc)
	}
	return b.err
}

// P print code
func (b *BMGenerate) P(args ...interface{}) {
	if b.err != nil {
		return
	}
	args = append(args, "\n")
	_, b.err = fmt.Fprint(b.target, args...)
}

func (b *BMGenerate) generatePackageImport() {
	b.P("// Package ", b.packageName, " Code generated by go-common/app/tool/protoc-gen-bm. DO NOT EDIT.")
	b.P("package ", b.packageName)
	b.P()
	b.P("import (")
	b.P("	\"context\"")
	if b.jsonpb {
		b.P("	\"bytes\"")
		b.P("	\"encoding/json\"")
		b.P()
		b.P("	\"go-common/app/tool/protoc-gen-bm/jsonpb\"")
	}
	b.P()
	b.P("	bm \"", bmPkgPath, "\"")
	b.P(")")
	b.P()
}

func (b *BMGenerate) generateServer(desc *BMServerDescriptor) {
	b.generateServerInterface(desc)
	b.generateServerHandler(desc)
	b.generateRegisterFunc(desc)
}

func (b *BMGenerate) generateServerInterface(desc *BMServerDescriptor) {
	serviceName := util.CamelCase(desc.Name)
	b.P(fmt.Sprintf("// BM%sServer interface as same as gGRPC server define", serviceName))
	b.P("type BM", serviceName, "Server interface {")
	for _, method := range desc.Methods {
		b.P("	", util.CamelCase(method.Name), fmt.Sprintf("(context.Context, *%s) (*%s, error)", method.RequestType, method.ReplyType))
	}
	b.P("}")
	b.P()
}

func (b *BMGenerate) generateServerHandler(desc *BMServerDescriptor) {
	serviceName := util.CamelCase(desc.Name)
	receiverName := fmt.Sprintf("_BMServer%s", serviceName)
	b.P("// _BMServer", serviceName, "server")
	b.P("type ", receiverName, " struct {")
	b.P("	BM", serviceName, "Server")
	b.P("}")
	b.P()
	for _, method := range desc.Methods {
		methodName := util.CamelCase(method.Name)
		funcName := fmt.Sprintf("bm%s%sHandler", serviceName, methodName)
		b.P(fmt.Sprintf("func (b *%s) ", receiverName), funcName, "(c *bm.Context) {")
		// bind req
		b.P(fmt.Sprintf("	req := new(%s)", method.RequestType))
		b.P(fmt.Sprintf("	if err := c.Bind(req); err != nil {"))
		b.P("		return")
		b.P("	}")
		// call service
		b.P(fmt.Sprintf("	reply, err := b.%s(c.Context, req)", methodName))
		if b.jsonpb {
			b.P("	if err != nil {")
			b.P("		c.JSON(nil, err)")
			b.P("		return")
			b.P("	}")
			b.P("	body := &bytes.Buffer{}")
			b.P("	marshaler := jsonpb.Marshaler{EmitDefaults: true, OrigName: true}")
			b.P("	err = marshaler.Marshal(body, reply)")
			b.P("	c.JSON(json.RawMessage(body.Bytes()), err)")
		} else {
			b.P("	c.JSON(reply, err)")
		}
		b.P("}")
		b.P()
	}
}

func (b *BMGenerate) generateRegisterFunc(desc *BMServerDescriptor) {
	serviceName := util.CamelCase(desc.Name)
	receiverName := fmt.Sprintf("_BMServer%s", serviceName)
	b.P(fmt.Sprintf("// Register%sBMServer register bm server", serviceName))
	b.P(fmt.Sprintf("func Register%sBMServer(e *bm.Engine, s BM%sServer) {", serviceName, serviceName))
	b.P(fmt.Sprintf("	bs := &%s{s}", receiverName))
	for _, method := range desc.Methods {
		methodName := util.CamelCase(method.Name)
		funcName := fmt.Sprintf("bm%s%sHandler", serviceName, methodName)
		b.P(fmt.Sprintf("	e.%s(\"%s\", bs.%s)", method.Method, method.PathPattern, funcName))
	}
	b.P("}")
	b.P()
}
