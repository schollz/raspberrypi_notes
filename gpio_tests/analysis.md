A good question to ask yourself before using the Raspberry Pi GPIO pins for time sensitive things is **exactly how fast can I read and write to these pins**? Writing from, or sending signals, from the GPIO pins has [already been investigated](http://codeandlife.com/2012/07/03/benchmarking-raspberry-pi-gpio-speed/), but the other way around has been more obscure. Here I answer the question and find some interesting, unexpected results!

## The test

All the following tests were done as root in a Raspberry Pi Model B+ using a Jessie build of Raspbian (Raspberry Pi Model 2 is generally [2-3 times faster](http://codeandlife.com/2015/03/25/raspberry-pi-2-vs-1-gpio-benchmark/)). To calcualte result rates, the commands were run using time (e.g. ```time program```) and the ```real``` time result was used to divide into the total number of cycles or iterations to figure out the resulting rate.

## How fast can you write to GPIO pins for outputing a signal?

I decided to test the two fastest languages - Python and Native C - to see how fast it could be done. Also, I included Go in the experiments, which is a language that has not been tested for generating square waves yet. Here are the results.

|Language (linked to code)  | Tested  | Result (cycle rate)  |
|---|---|---|
| [Python](https://github.com/schollz/raspberrypi_notes/blob/master/gpio_tests/writing/gpio_write.py) |  06/06/2015 |  69 kHz |  
|  [Go](https://github.com/schollz/raspberrypi_notes/blob/master/gpio_tests/writing/gpio_write.go) |   06/06/2015 |  174 kHz |   
| [C](https://github.com/schollz/raspberrypi_notes/blob/master/gpio_tests/writing/gpio_write.c)  |  06/06/2015  | 15 MHz  |  

My results for Python and C are similar to what was [already investigated](http://codeandlife.com/2012/07/03/benchmarking-raspberry-pi-gpio-speed/), but the Go result is new! The Go result is pretty unexpected - it is very fast thanks to a [great library](https://github.com/stianeikeland/go-rpio) by [Stian Eikeland](https://github.com/stianeikeland).

## How fast can you read from GPIO pins *to memory*?

Another question is how fast can you read? In this case I want to read a pin many times and store the value in virtual memory so there is no hard-disk retrieval here. I'm going to focus on the two fastest languages - Go and native C. 

|Language (linked to code)  | Tested  | Result (read rate)  |
|---|---|---|
|  [Go](https://github.com/schollz/raspberrypi_notes/blob/master/gpio_tests/reading/tovariable/read_in_memory.go) |   06/06/2015 |  1.6 Mhz |   
| [C](https://github.com/schollz/raspberrypi_notes/blob/master/gpio_tests/reading/tovariable/read_in_memory.c)  |  06/06/2015  | 7.2 MHz  |  

Is reading harder or easier for a program? For C, it actually seems to be harder, as it reads about half the rate it can write a cycle (and the cycle writing is actually two pin changes - so it effectively makes 4 times fewer pin changes!). However, for Go it can read faster than it can write! Go seems like a good alternative to C for reading GPIO pins.  

These read speeds are effectively the *fastest* you can possibly read. These programs read into memory and do nothing with the result. In a practical case you'd want to use the result - most likely by writing it to disk, thus you'll have a bottleneck there immedietly. This brings me to the final question:

## How fast can you read from GPIO pins *to disk*?

This experiment is similar to the previous, except that here I use Go and C to compile the individual bits into bytes which are written to disk as a block every 1000 Bytes. The results are surprising:

|Language (linked to code)  | Tested  | Result (read rate)  |
|---|---|---|
|  [Go](https://github.com/schollz/raspberrypi_notes/blob/master/gpio_tests/reading/tofile/read_to_file.go) |   06/06/2015 |  440 kHz |   
| [C](https://github.com/schollz/raspberrypi_notes/blob/master/gpio_tests/reading/tofile/read_to_file.c)  |  06/06/2015  | 673 kHz  |  

Here was the real surprise - Go creeps up on C in terms of speed! Go seems to be optimized for both *reading the GPIO pin* as well as continuous *writing to disk*. Given the ease of coding, it seems like the Go may be the best way to go for reading GPIO pins.

## TL;DR

Use Go for reading GPIO pins because its about as fast as C and a bit easier to code in, but use C if you want to write to pins (max cycle rate 15 MHz).
