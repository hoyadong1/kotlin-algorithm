package brute_force

data class Node(val value: Int = 0, val next : Int = -1, var shortcut : Int = -1)

fun main(){
    val command = readln().split(" ").map { it.toInt() }
    val map = Array(33){ Node() }
    val isOccupied = BooleanArray(33)
    val horsePos = IntArray(4)
    setupMap(map)
    var maxVal = 0

    fun dfs(depth : Int, current : Int){
        if(depth == 10){
            maxVal = maxOf(maxVal, current)
            return
        }

        for (i in 0..3){
            val start = horsePos[i]
            if (start == 32) continue

            var next = start
            val move = command[depth]

            if (map[start].shortcut != -1){
               next = map[start].shortcut
                for(i in 1..<move){
                    next = map[next].next
                    if(next == 32) break
                }
            } else {
                for(i in 0..<move){
                    next = map[next].next
                    if(next == 32) break
                }
            }

            if (next != 32 && isOccupied[next]) continue
            isOccupied[start] = false
            isOccupied[next] = true
            horsePos[i] = next

            dfs(depth + 1, current + map[next].value)

            isOccupied[start] = true
            isOccupied[next] = false
            horsePos[i] = start
        }
    }

    dfs(0, 0)
    print(maxVal)
}

fun setupMap(map: Array<Node>) {
    for (i in 0..19) map[i] = Node(i * 2, i + 1)
    map[20] = Node(40, 32)
    map[32] = Node(0, 32)

    map[5].shortcut = 21
    map[21] = Node(13, 22)
    map[22] = Node(16, 23)
    map[23] = Node(19, 24)

    map[10].shortcut = 25
    map[25] = Node(22, 26)
    map[26] = Node(24, 24)

    map[15].shortcut = 27
    map[27] = Node(28, 28)
    map[28] = Node(27, 29)
    map[29] = Node(26, 24)

    map[24] = Node(25, 30)
    map[30] = Node(30, 31)
    map[31] = Node(35, 20)
}

