function getAnswer(input) {
    var previousValue = 99999
    var timesIncreased = 0
    for (var line of input) {
        var value = Number(line)
        if (value > previousValue) {
            timesIncreased = timesIncreased + 1
        }
        previousValue = value
    }
    return timesIncreased
}