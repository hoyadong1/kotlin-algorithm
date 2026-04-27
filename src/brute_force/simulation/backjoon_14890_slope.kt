package brute_force

fun main(){
    val (N, L) = readln().split(" ").map { it.toInt()}
    val map = Array(N){ readln().split(" ").map { it.toInt() }.toIntArray() }

    var cnt = 0

    for (row in map) {
        if (canGo(row, L)) cnt++
    }

    val rotate = Array(N) { i ->
        IntArray(N){j -> map[j][i]}
    }

    for (row in rotate) {
        if (canGo(row, L)) cnt++
    }
    print(cnt)
}

fun canGo(arr: IntArray, L: Int): Boolean {
    val n = arr.size
    val visited = BooleanArray(n)

    for (i in 0..<n-1){
        if (arr[i] == arr[i+1]) continue

        val diff = arr[i] - arr[i+1]
        if (diff !in -1..1) return false

        if (diff == 1){
            for (j in 1..L){
                if(i + j >=n || arr[i+1] != arr[i+j] || visited[i+j]) return false
                visited[i+j] = true
            }
        }else{
            for (j in 0..<L){
                if(i - j < 0 || arr[i] != arr[i-j] || visited[i-j]) return false
                visited[i-j] = true
            }
        }
    }
    return true
}