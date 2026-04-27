package brute_force

import kotlin.math.abs

fun main(){
    val (N, K) = readln().split(" ").map{ it.toInt() }
    var tanks = readln().split(" ").map { it.toInt() }.toIntArray()
    var count = 0

    while(true){
        if (countDiff(tanks) <= K){
            print(count)
            return
        }
        count++

        val minVal = tanks.min()
        for (i in tanks.indices) {
            if (tanks[i] == minVal) tanks[i]++
        }

        val air1Mat = air1(tanks)
        tanks = flatten(adjust(air1Mat))
        val air2Mat = air2(tanks)
        tanks = flatten(adjust(air2Mat))
    }
}

fun air1(arr: IntArray): Array<IntArray> {
    val n = arr.size
    val matrix = Array(n) { IntArray(n) }

    for (i in 0 until n) {
        matrix[n - 1][i] = arr[i]
    }

    var startCol = 0
    var w = 1
    var h = 1

    while (true) {
        if (startCol + w + h > n) break

        for (r in 0 until h) {
            for (c in 0 until w) {
                val currentFish = matrix[n - 1 - r][startCol + c]
                matrix[n - 1 - r][startCol + c] = 0
                val nextR = n - 1 - (w - c)
                val nextC = startCol + w + r
                matrix[nextR][nextC] = currentFish
            }
        }

        startCol += w
        val nextW = h
        val nextH = w + 1
        w = nextW
        h = nextH
    }

    return matrix
}

fun air2(arr: IntArray): Array<IntArray> {
    val n = arr.size
    var currentRows = 1
    var currentColSize = n
    val matrix = Array(n) { IntArray(n) }
    for (i in arr.indices) matrix[n - 1][i] = arr[i]

    var left = 0
    repeat(2) {
        val moveW = currentColSize / 2
        for (r in 0 until currentRows) {
            for (c in 0 until moveW) {
                val currR = n - 1 - r
                val currC = left + c
                val fish = matrix[currR][currC]
                matrix[currR][currC] = 0

                val nextR = n - currentRows * 2 + r
                val nextC = n - 1 - c
                matrix[nextR][nextC] = fish
            }
        }
        left += moveW
        currentRows *= 2
        currentColSize /= 2
    }
    return matrix
}

fun countDiff(arr : IntArray) : Int{
    return arr.max() - arr.min()
}

fun adjust(matrix: Array<IntArray>): Array<IntArray> {
    val r = matrix.size
    val c = matrix[0].size
    val diff = Array(r) { IntArray(c) }

    val dx = intArrayOf(1, 0)
    val dy = intArrayOf(0, 1)

    for (y in 0 until r) {
        for (x in 0 until c) {
            if (matrix[y][x] == 0) continue

            for (d in 0..1) {
                val ny = y + dy[d]
                val nx = x + dx[d]

                if (ny in 0 until r && nx in 0 until c && matrix[ny][nx] != 0) {
                    val dValue = abs(matrix[y][x] - matrix[ny][nx]) / 5
                    if (dValue > 0) {
                        if (matrix[y][x] > matrix[ny][nx]) {
                            diff[y][x] -= dValue
                            diff[ny][nx] += dValue
                        } else {
                            diff[y][x] += dValue
                            diff[ny][nx] -= dValue
                        }
                    }
                }
            }
        }
    }

    val result = Array(r) { y ->
        IntArray(c) { x -> matrix[y][x] + diff[y][x] }
    }
    return result
}

fun flatten(matrix: Array<IntArray>): IntArray {
    val list = mutableListOf<Int>()
    val r = matrix.size
    val c = matrix[0].size
    for (x in 0 until c) {
        for (y in r - 1 downTo 0) {
            if (matrix[y][x] != 0) list.add(matrix[y][x])
        }
    }
    return list.toIntArray()
}