package basic.deep1

fun main(){
    val input = readln().split(" ").map { it.toInt() }

    val array = arrayOf(1,1,2,2,2,8)

    for (i in input.indices){
        print(array[i] - input[i])
        print(" ")
    }
}