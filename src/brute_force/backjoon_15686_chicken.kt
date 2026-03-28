package brute_force

import kotlin.math.abs
import kotlin.math.min

var N = 0
var M = 0
val houses = mutableListOf<Point>()
val chickens = mutableListOf<Point>()
var minCityDistance = Int.MAX_VALUE

fun main() {
    val input = readln().split(" ").map { it.toInt() }
    N = input[0]
    M = input[1]

    for (i in 0..<N) {
        val row = readln().split(" ").map { it.toInt() }
        for (j in 0..<N) {
            if (row[j] == 1) houses.add(Point(i, j))
            else if (row[j] == 2) chickens.add(Point(i, j))
        }
    }

    combine(0, 0, BooleanArray(chickens.size))

    println(minCityDistance)
}

fun combine(start: Int, count: Int, visited: BooleanArray) {
    if (count == M) {
        calculateDistance(visited)
        return
    }

    for (i in start..<chickens.size) {
        visited[i] = true
        combine(i + 1, count + 1, visited)
        visited[i] = false
    }
}

fun calculateDistance(visited: BooleanArray) {
    var cityDistance = 0

    for (house in houses) {
        var minHouseDistance = Int.MAX_VALUE
        for (i in chickens.indices) {
            if (visited[i]) {
                val dist = abs(house.x - chickens[i].x) + abs(house.y - chickens[i].y)
                minHouseDistance = min(minHouseDistance, dist)
            }
        }
        cityDistance += minHouseDistance
    }

    minCityDistance = min(minCityDistance, cityDistance)
}