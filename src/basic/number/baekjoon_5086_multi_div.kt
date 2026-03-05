package basic.number

fun main(){
    while(true){
        val (a, b) = readln().split(" ").map { it.toInt() }
        if(a == 0 && b == 0) break

        if (b % a == 0) println("factor")
        else if (a % b == 0) println("multiple")
        else println("neither")
    }
}