package brute_force

fun main(){
    val (N, M, T) = readln().split(" ").map { it.toInt() }
    val discs = Array(N){
        readln().split(" ").map { it.toInt() }.toIntArray()
    }
    val commands = Array(T){
        readln().split(" ").map { it.toInt() }.toIntArray()
    }

    for (command in commands){
        rotate(discs, M, command[0], command[1], command[2])

        if(!remove(discs, N, M)){
            avgDiscs(discs)
        }
    }

    print(discs.sumOf { it.sum().toLong() })
}

fun avgDiscs(discs: Array<IntArray>) {
    var sum = 0.0
    var count = 0

    for (r in discs.indices) {
        for (c in discs[r].indices) {
            if (discs[r][c] > 0) {
                sum += discs[r][c]
                count++
            }
        }
    }

    if (count == 0) return

    val avg = sum / count
    for (r in discs.indices) {
        for (c in discs[r].indices) {
            if (discs[r][c] > 0) {
                if (discs[r][c] > avg) discs[r][c] -= 1
                else if (discs[r][c] < avg) discs[r][c] += 1
            }
        }
    }
}

fun rotate(discs: Array<IntArray>, M : Int, x : Int, d : Int, k : Int){
    for (i in discs.indices){
        if ((i+1)%x == 0){
            val temp = IntArray(M)
            val rotateCnt = k % M

            for (j in 0..<M) {
                val nextPos = if (d == 0) {
                    (j + rotateCnt) % M
                } else {
                    (j + M - rotateCnt) % M
                }
                temp[nextPos] = discs[i][j]
            }
            discs[i] = temp
        }
    }
}

fun remove(discs: Array<IntArray>, N : Int, M: Int) : Boolean{
    var isRemoved = false
    val toRemove = mutableSetOf<Pair<Int, Int>>()

    for (i in 0..<N){
        for (j in 0..<M){
            if (discs[i][j] == 0) continue

            if (discs[i][j] == discs[i][(j+1)%M]){
                toRemove.add(i to j)
                toRemove.add(i to (j+1)%M)
            }

            if (i + 1 < N && discs[i][j] == discs[i+1][j]){
                toRemove.add(i to j)
                toRemove.add(i+1 to j)
            }
        }
    }

    if(toRemove.isNotEmpty()){
        isRemoved = true
        for ((x, y) in toRemove){
            discs[x][y] = 0
        }
    }

    return isRemoved
}