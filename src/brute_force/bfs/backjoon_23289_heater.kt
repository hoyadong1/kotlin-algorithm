package brute_force

var R = 0
var C = 0
var K = 0
lateinit var map : Array<IntArray>
lateinit var walls : Array<Array<BooleanArray>>
val heaters = mutableListOf<Triple<Int, Int, Int>>()
val targets = mutableListOf<Pair<Int, Int>>()

val dx = arrayOf(0, 0, -1, 1)
val dy = arrayOf(1, -1, 0, 0)

fun main() {
    val input = readln().split(" ").map { it.toInt() }
    R = input[0]
    C = input[1]
    K = input[2]
    map = Array(R){IntArray(C)}
    walls = Array(R){Array(C){BooleanArray(4)}}

    for (i in 0..<R){
        val row = readln().split(" ").map { it.toInt() }
        for (j in 0..<C){
            val v = row[j]
            if(v in 1..4) heaters.add(Triple(i, j, v-1))
            else if(v == 5) targets.add(Pair(i, j))
        }
    }

    val wallCount = readln().toInt()
    repeat(wallCount){
        val (x, y, t) = readln().split(" ").map { it.toInt()}

        if(t == 0){
            walls[x-1][y-1][2] = true
            if(x-2 >= 0) walls[x-2][y-1][3] = true
        } else{
            walls[x-1][y-1][0] = true
            if(y < C) walls[x-1][y][1] = true
        }
    }

    var chocolate = 0
    while(chocolate <= 100){
        for (h in heaters){
            blow(h.first, h.second, h.third)
        }

        adjust()
        reduce()
        chocolate++

        if (isFinished()) break
    }
    print(chocolate)
}

fun blow(x: Int, y: Int, d: Int) {
    val q = ArrayDeque<IntArray>()
    val visited = Array(R){BooleanArray(C)}

    val sx = x + dx[d]
    val sy = y + dy[d]

    if (sx !in 0..<R || sy !in 0..<C) return

    map[sx][sy] += 5
    visited[sx][sy] = true
    q.addLast(intArrayOf(sx, sy, 5))

    while (q.isNotEmpty()){
        val (cx, cy, cw) = q.removeFirst()
        if(cw == 1) continue

        val nextD = when(d){
            0, 1 -> intArrayOf(d, 2, 3)
            2, 3 -> intArrayOf(d, 0, 1)
            else -> intArrayOf()
        }

        for (nd in nextD){
            if(!walls[cx][cy][nd]){
                val nx = cx + dx[nd]
                val ny = cy + dy[nd]
                if(nx in 0..<R && ny in 0..<C){
                    if(nd == d){
                        if(!visited[nx][ny]){
                            visited[nx][ny] = true
                            map[nx][ny] += cw-1
                            q.addLast(intArrayOf(nx, ny, cw-1))
                        }
                    } else {
                        if (!walls[nx][ny][d]){
                            val nnx = nx + dx[d]
                            val nny = ny + dy[d]
                            if(nnx in 0..<R && nny in 0..<C && !visited[nnx][nny]){
                                visited[nnx][nny] = true
                                map[nnx][nny] += cw-1
                                q.addLast(intArrayOf(nnx, nny, cw-1))
                            }
                        }
                    }
                }
            }
        }
    }
}

fun adjust() {
    val diffArr = Array(R) { IntArray(C) }
    for (i in 0..<R) {
        for (j in 0..<C) {
            for (d in intArrayOf(0, 3)) {
                if (!walls[i][j][d]) {
                    val nx = i + dx[d]
                    val ny = j + dy[d]
                    if (nx in 0..<R && ny in 0..<C) {
                        val diff = map[i][j] - map[nx][ny]
                        val divDiff = (if (diff < 0) -diff else diff) / 4
                        if (diff > 0) {
                            diffArr[i][j] -= divDiff
                            diffArr[nx][ny] += divDiff
                        } else {
                            diffArr[i][j] += divDiff
                            diffArr[nx][ny] -= divDiff
                        }
                    }
                }
            }
        }
    }
    for (i in 0..<R) {
        for (j in 0..<C) map[i][j] += diffArr[i][j]
    }
}

fun reduce() {
    for (i in 0..<R) {
        for (j in 0..<C) {
            if (i == 0 || i == R - 1 || j == 0 || j == C - 1) {
                if (map[i][j] > 0) map[i][j]--
            }
        }
    }
}

fun isFinished(): Boolean {
    for(t in targets){
        if (map[t.first][t.second] < K) return false
    }
    return true
}