package basic.math

fun main(){
    val n = readln().toInt()
    var num = 1
    var total = 0
    var isOdd = true

    while (true){
        if (total >= n) break
        total += num
        num++
        isOdd = !isOdd
    }

    val a = n - (total - num + 1)

    val c = if(isOdd) a else num - a
    val p = if(isOdd) num - a else a

    print("$c/$p")
}