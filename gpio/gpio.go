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
