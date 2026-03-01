package basic.math

fun main(){
    val n = readln().toInt()
    var count = 1
    var num = 1

    while(true){
        if(n <= num) break

        num += 6*count
        count++
    }

    print(count)
}