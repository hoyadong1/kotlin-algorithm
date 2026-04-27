package brute_force

fun main(){
    val (N, K) = readln().split(" ").map{it.toInt()}
    val map = Array(N){
        readln().split(" ").map { it.toInt() }.toIntArray()
    }
    val pieces = Array(K){
        readln().split(" ").map { it.toInt() - 1 }.toMutableList()
    }
    var time = 0
    val dx = arrayOf(0, 0, -1, 1)
    val dy = arrayOf(1, -1, 0, 0)

    val board = Array(N) { Array(N) { mutableListOf<Int>() } }
    for (i in 0 until K) {
        val (x, y, d) = pieces[i]
        board[x][y].add(i)
    }

    while (time <= 1000) {
        time++
        for (i in 0 until K) {
            val (x, y, d) = pieces[i]

            val index = board[x][y].indexOf(i)
            val movingPieces = board[x][y].subList(index, board[x][y].size).toList()

            var nx = x + dx[d]
            var ny = y + dy[d]

            if (nx !in 0 until N || ny !in 0 until N || map[nx][ny] == 2) {
                val nextD = d xor 1
                pieces[i][2] = nextD
                nx = x + dx[nextD]
                ny = y + dy[nextD]

                if (nx !in 0 until N || ny !in 0 until N || map[nx][ny] == 2) continue
            }

            val targetPieces = if (map[nx][ny] == 1) movingPieces.reversed() else movingPieces

            val size = board[x][y].size
            repeat(size - index) { board[x][y].removeAt(index) }

            for (pIdx in targetPieces) {
                board[nx][ny].add(pIdx)
                pieces[pIdx][0] = nx
                pieces[pIdx][1] = ny
            }

            if (board[nx][ny].size >= 4) {
                println(time)
                return
            }
        }
    }
    println(-1)
}