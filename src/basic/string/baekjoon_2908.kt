package basic.string

fun main(){
    val s = readln().split(" ")
    val a = s[0].reversed().toInt()
    val b = s[1].reversed().toInt()
    val c = if (a > b) a else b
    println(c)
}