func twoSum(nums []int, target int) []int {
    // Solution 1 - Brute Force
    /*
    res := make([]int, 0)
    for i, numi := range(nums) {
        for j, numj := range(nums) {
            if i != j && numi + numj == target {
                res = append(res, i)
                res = append(res, j)
                return res
            }
        }
    }
    return nil
    */
    // Solution 2 - HashMap
    prevMap := make(map[int]int)
    for i, n := range(nums) {
        if val, found := prevMap[target-n]; found {
            return []int{val, i}
        }
        prevMap[n] = i
    }
    return nil
}
