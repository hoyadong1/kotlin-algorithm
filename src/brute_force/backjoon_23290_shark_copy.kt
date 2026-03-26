package brute_force

fun main() {
    val (M, S) = readln().split(" ").map { it.toInt() }
    var fishMap = Array(4) { Array(4) { mutableListOf<Int>() } }
    val smell = Array(4) { IntArray(4) }

    val dx = intArrayOf(0, -1, -1, -1, 0, 1, 1, 1)
    val dy = intArrayOf(-1, -1, 0, 1, 1, 1, 0, -1)

    repeat(M) {
        val (x, y, d) = readln().split(" ").map { it.toInt() - 1}
        fishMap[x][y].add(d)
    }

    var (sx, sy) = readln().split(" ").map { it.toInt() - 1 }

    val sdx = intArrayOf(-1, 0, 1, 0)
    val sdy = intArrayOf(0, -1, 0, 1)

    repeat(S) {
        // 1. 복제 예약
        val copy = Array(4) { r -> Array(4) { c -> fishMap[r][c].toList() } }

        // 2. 물고기 이동
        val nextMap = Array(4) { Array(4) { mutableListOf<Int>() } }
        for (r in 0..3) {
            for (c in 0..3) {
                for (d in fishMap[r][c]) {
                    var moved = false
                    for (i in 0..7) {
                        val nd = (d - i + 8) % 8
                        val nx = r + dx[nd]
                        val ny = c + dy[nd]
                        if (nx in 0..3 && ny in 0..3 && !(nx == sx && ny == sy) && smell[nx][ny] == 0) {
                            nextMap[nx][ny].add(nd)
                            moved = true
                            break
                        }
                    }
                    if (!moved) nextMap[r][c].add(d)
                }
            }
        }

        // 3. 상어 이동 경로 찾기
        var maxEat = -1
        var bestPath = intArrayOf()

        fun findShark(x: Int, y: Int, depth: Int, currentEat: Int, path: IntArray, visited: Array<BooleanArray>) {
            if (depth == 3) {
                if (currentEat > maxEat) {
                    maxEat = currentEat
                    bestPath = path.copyOf()
                }
                return
            }

            for (i in 0..3) {
                val nx = x + sdx[i]
                val ny = y + sdy[i]
                if (nx in 0..3 && ny in 0..3) {
                    val firstVisit = !visited[nx][ny]
                    val fishInSpot = if (firstVisit) nextMap[nx][ny].size else 0

                    visited[nx][ny] = true
                    path[depth] = i
                    findShark(nx, ny, depth + 1, currentEat + fishInSpot, path, visited)
                    if (firstVisit) visited[nx][ny] = false
                }
            }
        }

        findShark(sx, sy, 0, 0, IntArray(3), Array(4) { BooleanArray(4) })

        // 4. 상어 이동 확정 및 냄새 남기기
        for (d in bestPath) {
            sx += sdx[d]
            sy += sdy[d]
            if (nextMap[sx][sy].isNotEmpty()) {
                nextMap[sx][sy].clear()
                smell[sx][sy] = 3
            }
        }

        // 5. 냄새 감소
        for (i in 0..3) {
            for (j in 0..3) {
                if (smell[i][j] > 0) smell[i][j]--
            }
        }

        // 6. 복제 완료
        for (i in 0..3) {
            for (j in 0..3) {
                nextMap[i][j].addAll(copy[i][j])
            }
        }
        fishMap = nextMap
    }

    var result = 0
    for (i in 0..3) for (j in 0..3) result += fishMap[i][j].size
    print(result)
}