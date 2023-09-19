package main

import "fmt"

func main() {
    var count int = 0

    for i := 1; i <= 9; i++ {
        for j := 1; j <= 9; j++ {
            for k := 1; k <= 9; k++ {
                if j != i+1 && k != j+1 {
                    count++
                }

                fmt.Printf("number: %d%d%d | count: %d\n", i, j, k, count)
            }
        }
    }
}



