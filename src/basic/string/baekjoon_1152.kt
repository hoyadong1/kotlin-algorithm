package basic.string

fun main(){
    val input = readln().split(" ").filter { it.isNotBlank() }
    println(input.size)
}