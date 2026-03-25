package brute_force

data class Cloud(var x : Int, var y : Int)

fun main(){
    val (N, M) = readln().split(" ").map { it.toInt() }
    val map = Array(N) { readln().split(" ").map { it.toInt() }.toIntArray() }

    val dx = intArrayOf(0, -1, -1, -1, 0, 1, 1, 1)
    val dy = intArrayOf(-1, -1, 0, 1, 1, 1, 0, -1)
    val wx = intArrayOf(-1, -1, 1, 1)
    val wy = intArrayOf(-1, 1, -1, 1)

    val moves = Array(M){
        val (d, s) = readln().split(" ").map { it.toInt() }
        Pair(d-1, s)
    }

    var clouds = mutableListOf(
        Cloud(N-1, 0),
        Cloud(N-1,1),
        Cloud(N-2,0),
        Cloud(N-2,1)
    )

    for ((d, s) in moves){
        val visited = Array(N){BooleanArray(N)}
        val newClouds = mutableListOf<Cloud>()

        for (c in clouds){
            val nx = (c.x + dx[d] * s % N + N) % N
            val ny = (c.y + dy[d] * s % N + N) % N

            map[nx][ny]++
            visited[nx][ny] = true
            newClouds.add(Cloud(nx, ny))
        }

        for (c in newClouds){
            var cnt = 0
            for (d in 0..<4){
                val nx = c.x + wx[d]
                val ny = c.y + wy[d]
                if (nx in 0..<N && ny in 0..<N && map[nx][ny] > 0){
                    cnt++
                }
            }
            map[c.x][c.y] += cnt
        }

        clouds = mutableListOf()
        for(i in 0..<N){
            for(j in 0..<N){
                if (!visited[i][j] && map[i][j] >= 2){
                    clouds.add(Cloud(i, j))
                    map[i][j] -= 2
                }
            }
        }
    }

    var sum = 0
    for(i in 0..<N){
        for (j in 0..<N){
            sum += map[i][j]
        }
    }

    print(sum)
}