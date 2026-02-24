package basic.math

fun main(){
    val (N, B) = readln().split(" ")
    val Bint = B.toInt()
    var sum = 0

    for(c in N){
        val value = if (c.isDigit()){
            c - '0'
        } else{
            c - 'A' + 10
        }
        sum = sum * Bint + value
    }

    println(sum)
}