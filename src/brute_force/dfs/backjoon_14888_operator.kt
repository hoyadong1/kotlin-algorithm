package brute_force

var n = 0
lateinit var numbers : IntArray
var operator = IntArray(4)

var maxVal = Int.MIN_VALUE
var minVal = Int.MAX_VALUE

fun main(){
    n = readln().toInt()
    numbers = readln().split(" ").map { it.toInt() }.toIntArray()
    operator = readln().split(" ").map { it.toInt() }.toIntArray()

    dfs(1, numbers[0])

    println(maxVal)
    println(minVal)
}

fun dfs(depth : Int, current : Int){
    if(depth == n){
        maxVal = maxOf(maxVal, current)
        minVal = minOf(minVal, current)
        return
    }

    for(i in 0..<4){
        if (operator[i] > 0){
            operator[i]--

            val nextVal = when(i){
                0 -> current + numbers[depth]
                1 -> current - numbers[depth]
                2 -> current * numbers[depth]
                3 -> current / numbers[depth]
                else -> current
            }

            dfs(depth + 1, nextVal)
            operator[i]++
        }
    }
}