package basic.array

fun main(){
    var max = 0
    var maxCol = 0
    var maxLow = 0

    repeat(9){ row ->
        val input = readln().split(" ").map{ it.toInt() }
        for (i in input.indices){
            if (input[i] > max) {
                max = input[i]
                maxCol = i
                maxLow = row
            }
        }
    }

    println(max)
    println("${maxLow+1} ${maxCol+1}")
}