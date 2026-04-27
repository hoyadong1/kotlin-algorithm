package brute_force

fun main() {
    val (N, M) = readln().split(" ").map{ it.toInt() }
    val map = Array(N) { readln().split(" ").map{it.toInt()}.toIntArray()}
    val commands = Array(M){
        val (d, s) = readln().split(" ").map{ it.toInt() }
        Pair(d-1, s)
    }
    val center = N/2

    val bx = intArrayOf(-1, 1, 0, 0)
    val by = intArrayOf(0, 0, -1, 1)

    // 달팽이 순서 리스트 만들기
    val order = mutableListOf<Pair<Int, Int>>()
    run {
        var x = center
        var y = center

        val dx = intArrayOf(0, 1, 0, -1)
        val dy = intArrayOf(-1, 0, 1, 0)

        var len = 1
        var dir = 0

        while (true) {
            repeat(2) {
                repeat(len) {
                    x += dx[dir]
                    y += dy[dir]
                    if (x !in 0..<N || y !in 0..<N) return@run
                    order.add(Pair(x, y))
                }
                dir = (dir + 1) % 4
            }
            len++
        }
    }

    val answer = IntArray(4)

    for ((d, s) in commands){

        // 공격
        for (i in 1..s){
            val nx = center + bx[d] * i
            val ny = center + by[d] * i
            if(nx in 0..<N && ny in 0..<N){
                map[nx][ny] = 0
            }
        }

        // map -> list
        val beed = mutableListOf<Int>()
        for ((x, y) in order){
            if(map[x][y] != 0) beed.add(map[x][y])
        }

        // list 기반 폭발 처리
        while(true){
            var i = 0
            var exploded = false
            val newList = mutableListOf<Int>()

            while(i < beed.size){
                var j = i
                while (j < beed.size && beed[j] == beed[i]) j++

                val cnt = j - i
                if(cnt >= 4){
                    exploded = true
                    answer[beed[i]] += cnt
                } else{
                    repeat(cnt){
                        newList.add(beed[i])
                    }
                }
                i = j
            }
            beed.clear()
            beed.addAll(newList)

            if(!exploded) break
        }

        // 구슬 합체 처리
        val transformed = mutableListOf<Int>()
        var i = 0
        while (i < beed.size){
            var j = i
            while (j < beed.size && beed[j] == beed[i]) j++

            transformed.add(j - i)
            transformed.add(beed[i])
            i = j
        }

        // 합체 된 구슬 기반으로 맵 갱신
        for (i in 0..<N){
            for(j in 0..<N){
                map[i][j] = 0
            }
        }
        for(i in transformed.indices){
            if(i >= order.size) break
            val (x, y) = order[i]
            map[x][y] = transformed[i]
        }
    }

    val result = answer[1] * 1 + answer[2] * 2 + answer[3] * 3
    print(result)
}