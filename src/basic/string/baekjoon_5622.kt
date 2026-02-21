package basic.string

fun main(){
    val input = readln()

    var sum = 0

    for(i in input){
        if (i == 'S') sum += 8
        else if (i == 'Z' || i == 'Y') sum += 10
        else if (i == 'V') sum += 9
        else sum += ((i - 'A')/3)+3
    }

    println(sum)
}