package main

import "fmt"

func main() {
	intArray := []int{4, 1, 1, 1, 4}
	fmt.Println(trap(intArray))
}
func trap(height []int) int {

	count := 0
	for range height {
		count++
	}
	return count

}
