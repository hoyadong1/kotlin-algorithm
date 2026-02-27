package basic.math

fun main() {
    val n = readln().toInt()
    val side = (1 shl n) + 1
    println(side * side)
}