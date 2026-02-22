package basic.deep1

fun main() {
    var creditSum = 0.0
    var sum = 0.0

    val map = mapOf(
        "A+" to 4.5,
        "A0" to 4.0,
        "B+" to 3.5,
        "B0" to 3.0,
        "C+" to 2.5,
        "C0" to 2.0,
        "D+" to 1.5,
        "D0" to 1.0,
        "F" to 0.0,
    )

    repeat(20) {
        val input = readln().split(" ")
        val credit = input[1].toDouble()
        val grade = input[2]

        if (grade == "P") return@repeat

        creditSum += credit
        sum += credit * map[grade]!!
    }

    println(sum / creditSum)
}