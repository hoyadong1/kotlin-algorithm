package basic.deep1

fun main(){
    val n = readln().toInt()
    var sum = 0

    repeat(n){
        val set : MutableSet<Char> = mutableSetOf()
        val input = readln()
        var isDuplicate = false
        var prev = ' '

        for (i in input){
            if (set.contains(i) && prev != i){
                isDuplicate = true
                break
            }
            else{
                set.add(i)
                prev = i
            }
        }
        if (!isDuplicate) sum++
    }

    println(sum)
}