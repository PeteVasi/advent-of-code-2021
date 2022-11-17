function getAnswer(input) {
    var currentSum = Number(input[0]) + Number(input[1]) + Number(input[2])
    var previousSum = currentSum
    var timesIncreased = 0
    for (var i=3; i<input.length; i++) {
        currentSum = currentSum + Number(input[i]) - Number(input[i-3])
        if (currentSum > previousSum) {
            timesIncreased = timesIncreased + 1
        }
        previousSum = currentSum
    }
    return timesIncreased
}