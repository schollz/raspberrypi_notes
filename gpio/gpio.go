//export GOROOT=/usr/local/go 
//export GOPATH=$HOME/go 
//export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
//go get github.com/kidoman/embd
//go run gpio.go
package main

import (
   "github.com/kidoman/embd"
   _ "github.com/kidoman/embd/host/rpi"
)

func main() {
   embd.InitGPIO()
   defer embd.CloseGPIO()
   for i:=0;i<100000000;i++ {
      embd.DigitalRead(1)
   }
}
