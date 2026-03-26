package brute_force

fun main() {
    val input = readln().split(" ").map { it.toInt() }
    val r = input[0] - 1
    val c = input[1] - 1
    val k = input[2]
    var matrix = Array(3) { readln().split(" ").map { it.toInt() }.toIntArray() }
    var time = 0

    while (time <= 100) {
        val rowS = matrix.size
        val colS = matrix[0].size
        if (r < rowS && c < colS && matrix[r][c] == k) {
            println(time)
            return
        }
        time++

        if (rowS >= colS){
            matrix = performR(matrix)
        }else{
            matrix = performC(matrix)
        }

    }
    print(-1)
}

fun performR(matrix: Array<IntArray>): Array<IntArray> {
    val newMatrix = mutableListOf<IntArray>()
    var maxLen = 0

    for (r in matrix) {
        val countMap = mutableMapOf<Int, Int>()
        for (num in r){
            if (num == 0) continue
            countMap[num] = countMap.getOrDefault(num, 0) + 1
        }

        val sortedList = countMap.toList().sortedWith(compareBy({ it.second }, { it.first }))

        val newRow = IntArray(minOf(100, sortedList.size * 2))
        var idx = 0
        for((num, count) in sortedList){
            if (idx >= 100) break
            newRow[idx++] = num
            newRow[idx++] = count
        }
        maxLen = maxOf(maxLen, newRow.size)
        newMatrix.add(newRow)
    }

    return Array(newMatrix.size) { i ->
        IntArray(maxLen){ j -> if(j < newMatrix[i].size) newMatrix[i][j] else 0 }
    }
}

fun performC(matrix: Array<IntArray>): Array<IntArray> {
    val newMatrix = mutableListOf<IntArray>()
    var maxLen = 0

    for (j in 0..<matrix[0].size){
        val countMap = mutableMapOf<Int, Int>()
        for (i in 0..<matrix.size){
            val num = matrix[i][j]
            if (num == 0) continue
            countMap[num] = countMap.getOrDefault(num, 0) + 1
        }

        val sortedList = countMap.toList().sortedWith(compareBy({it.second}, {it.first}))
        val newCol = IntArray(minOf(100, sortedList.size * 2))
        var idx = 0
        for((num, count) in sortedList){
            if (idx >= 100) break
            newCol[idx++] = num
            newCol[idx++] = count
        }
        maxLen = maxOf(maxLen, newCol.size)
        newMatrix.add(newCol)
    }
    return Array(minOf(100, maxLen)){ i ->
        IntArray(newMatrix.size){j -> if(i < newMatrix[j].size) newMatrix[j][i] else 0}
    }
}