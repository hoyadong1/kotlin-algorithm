package basic.math

fun main(){
    val n = readln().toInt()

    repeat(n){
        var money = readln().toInt()

        print(money/25)

        money %= 25

        print(" ${money/10}")

        money %= 10

        print(" ${money/5}")

        money %= 5

        print(" $money")
        println()
    }
}