package basic

fun main(){
    val n = readln().toInt()

    repeat(n){
        val input = readln().split(" ")

        for (i in input[1]){
            repeat(input[0].toInt()){
                print(i)
            }
        }
        println()
    }
}