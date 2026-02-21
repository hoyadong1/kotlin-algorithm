package basic.string

import kotlin.text.iterator

fun main(){
    readln()
    val input = readln()
    var sum = 0

    for(i in input){
        sum += i - '0'
    }

    println(sum)
}