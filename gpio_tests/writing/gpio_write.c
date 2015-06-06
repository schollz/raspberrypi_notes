package main

import (
   "github.com/stianeikeland/go-rpio"
)

var (
   pin = rpio.Pin(23) //GPIO4
)

func main() {
   err := rpio.Open()
   if err != nil {
      panic(err)
   }
   defer rpio.Close()

   for i := 0; i < 5000000; i++ {
      pin.Write(1)
      pin.Write(0)
   }

}
