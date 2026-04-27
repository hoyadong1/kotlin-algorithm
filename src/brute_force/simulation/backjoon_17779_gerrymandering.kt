package brute_force

fun main(){
    val n = readln().toInt()
    val map = Array(n){ readln().split(" ").map{ it.toInt() }.toIntArray()}
    var minVal = Int.MAX_VALUE
    val totalPopulation = map.sumOf { row -> row.sum() }

    for(x in 0..<n){
        for(y in 0..<n){
            for(d1 in 0..<n){
                for(d2 in 0..<n){
                    if(x + d1 + d2 in 0..<n && y - d1 in 0..<n && y + d2 in 0..<n){
                        minVal = minOf(minVal, calculate(n, map, totalPopulation, x, y, d1, d2))
                    }
                }
            }
        }
    }
    print(minVal)
}

fun calculate(n : Int, map: Array<IntArray>, total : Int, x : Int, y : Int, d1 : Int, d2 : Int): Int{
    val populations = IntArray(5)
    val isBoundary = Array(n){BooleanArray(n)}

    for (i in 0..d1){
        isBoundary[x + i][y - i] = true
        isBoundary[x + d2 + i][y + d2 - i] = true
    }
    for (i in 0..d2){
        isBoundary[x + i][y + i] = true
        isBoundary[x + d1 + i][y - d1 + i] = true
    }

    for (i in 0..<x + d1) {
        for (j in 0..y) {
            if (isBoundary[i][j]) break
            populations[0] += map[i][j]
        }
    }

    for (i in 0..x + d2) {
        for (j in n-1 downTo y + 1) {
            if (isBoundary[i][j]) break
            populations[1] += map[i][j]
        }
    }

    for (i in x + d1..<n) {
        for (j in 0..<y - d1 + d2) {
            if (isBoundary[i][j]) break
            populations[2] += map[i][j]
        }
    }

    for (i in x + d2 + 1..<n) {
        for (j in n-1 downTo y - d1 + d2) {
            if (isBoundary[i][j]) break
            populations[3] += map[i][j]
        }
    }

    populations[4] = total - (0..3).sumOf { populations[it] }
    return populations.max() - populations.min()
}