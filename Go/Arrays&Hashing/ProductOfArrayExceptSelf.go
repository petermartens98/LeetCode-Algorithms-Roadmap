func productExceptSelf(nums []int) []int {
    res := make([]int, len(nums))
    prefix := 1
    for i := 0; i < len(nums); i++ {
        res[i] = prefix
        prefix *= nums[i]
    }
    postfix := 1
    for i := len(nums)-1; i >= 0; i-- {
        res[i] *= postfix
        postfix *= nums[i]
    }
    return res
}
