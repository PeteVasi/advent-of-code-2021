package main

import (
	"encoding/csv"
	"fmt"
	"os"
	"strconv"
)

func main() {
	file, _ := os.Open("input1.txt")
	defer file.Close()
	csvReader := csv.NewReader(file)
	lines, _ := csvReader.ReadAll()
	var nums []int
	for _, line := range lines {
		n, _ := strconv.Atoi(line[0])
		nums = append(nums, n)
	}
	part1(nums)
	part2(nums)
}

func part1(nums []int) {
	inc := 0
	last := 99999
	for _, n := range nums {
		if n > last {
			inc++
		}
		last = n
	}
	fmt.Printf("Total increments: %d\n", inc)
}

func part2(nums []int) {
	inc := 0
	last := nums[0] + nums[1] + nums[2]
	for i := 3; i < len(nums); i++ {
		cur := last + nums[i] - nums[i-3]
		if cur > last {
			inc++
		}
		last = cur
	}
	fmt.Printf("Total increments: %d\n", inc)
}
