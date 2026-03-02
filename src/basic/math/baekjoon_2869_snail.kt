package basic.math

fun main(){
    val (up, down, goal) = readln().split(" ").map { it.toInt() }

    val daily = up - down
    val count = (goal - up + daily - 1) / daily + 1

    print(count)
}