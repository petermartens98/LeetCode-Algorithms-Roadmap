func topKFrequent(nums []int, k int) (res []int) {
	countMap := map[int]int{}
	freq := make([][]int, len(nums)+1)

	for _, num := range nums {
		if count, ok := countMap[num]; ok {
			countMap[num] = count + 1
		} else {
			countMap[num] = 1
		}
	}

	for num, count := range countMap {
		freq[count] = append(freq[count], num)
	}

	for i := len(freq) - 1; i > 0; i-- {
		res = append(res, freq[i]...)
		if len(res) == k {
			return
		}
	}
	return
}
