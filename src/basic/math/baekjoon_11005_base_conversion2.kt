package basic.math

fun main(){
    val (N, B) = readln().split(" ").map { it.toInt() }

    var num = N
    val sb = StringBuilder()

    while (num > 0){
        val remainder = num % B
        sb.append(if (remainder < 10) remainder else 'A' + (remainder - 10))

        num /= B
    }
    println(sb.reverse())
}