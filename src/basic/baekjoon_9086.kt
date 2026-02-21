package basic

fun main() {
    val n = readln().toInt()

    repeat(n) {
        val s = readln()
        println("${s.first()}${s.last()}")
    }
}