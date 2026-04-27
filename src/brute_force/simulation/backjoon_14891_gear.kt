package brute_force

import kotlin.math.pow

fun main(){
    val gears = Array(4) {
        readln().map { it.toString().toInt() }.toIntArray()
    }
    val K = readln().toInt()
    val commands = Array(K){
        val (num, d) = readln().split(" ").map{it.toInt()}
        Pair(num-1, d)
    }

    for ((num, d) in commands) {
       rotate(gears, num, d)
    }


    var answer = 0
    for (i in gears.indices) {
        if (gears[i][0] == 1){
            answer += 2.0.pow(i).toInt()
        }
    }
    print(answer)
}

fun rotate(gears: Array<IntArray>, num: Int, d: Int) {
    val dirs = IntArray(4)
    dirs[num] = d

    for (i in num downTo 1) {
        if (gears[i][6] != gears[i - 1][2]) {
            dirs[i - 1] = -dirs[i]
        } else break
    }

    for (i in num..<3) {
        if (gears[i][2] != gears[i + 1][6]) {
            dirs[i + 1] = -dirs[i]
        } else break
    }

    for (i in 0..<4) {
        if (dirs[i] == 0) continue

        val tempGear = IntArray(8)
        if (dirs[i] == 1) {
            for (j in 0..<8) tempGear[(j + 1) % 8] = gears[i][j]
        } else {
            for (j in 0..<8) tempGear[j] = gears[i][(j + 1) % 8]
        }
        gears[i] = tempGear
    }
}