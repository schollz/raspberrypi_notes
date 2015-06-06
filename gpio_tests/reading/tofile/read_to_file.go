package main

import (
	"os"
	"github.com/stianeikeland/go-rpio"
)

func readBytes(pin rpio.Pin, size int) *[]byte {
	arr := make([]byte, size)
	var b byte
	for i := 0; i < len(arr); i++ {
		for j := 0; j < 8; j++ {
			b = (b << 1) | byte(pin.Read())
		}
		arr[i] = b
	}
	return &arr
}

func main() {
	err := rpio.Open()
	if err != nil {
		panic(err)
	}
	defer rpio.Close()
	pin := rpio.Pin(23) //GPIO4
	pin.Input()         //set input mode

	n := 5000000 / 1000 // read in 1000 Byte chunks

	f, err := os.Create("test")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	for read := 0; read < n; read++ {
		ptr := readBytes(pin, 1000)
		f.Write(*ptr)
	}
}
