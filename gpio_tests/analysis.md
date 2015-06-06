A good question to ask yourself before using the Raspberry Pi GPIO pins for time sensitive things is **exactly how fast can I read and write to these pins**? Writing from, or sending signals, from the GPIO pins has [already been investigated](http://codeandlife.com/2012/07/03/benchmarking-raspberry-pi-gpio-speed/), but the other way around has been more obscure. Here I answer the question and find some interesting, unexpected results!

## How fast can you write to GPIO pins for outputing a signal?

I decided to test the two fastest languages - Python and Native C - to see how fast it could be done. Also, I had help to include Go into the mix. Here are the results.

|Language (linked to code)  | Tested  | Result (cycle rate)  |
|---|---|---|
| [Python](https://github.com/schollz/raspberrypi_notes/blob/master/gpio_tests/writing/gpio_write.py) |  06/06/2015 |  69 kHz |  
|  [Go](https://github.com/schollz/raspberrypi_notes/blob/master/gpio_tests/writing/gpio_write.go) |   06/06/2015 |  174 kHz |   
| [C](https://github.com/schollz/raspberrypi_notes/blob/master/gpio_tests/writing/gpio_write.c)  |  06/06/2015  | 15 MHz  |  
