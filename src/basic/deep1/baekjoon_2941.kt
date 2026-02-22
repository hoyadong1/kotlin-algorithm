package basic.deep1

fun main() {
    val input = readln()
    var i = 0
    var sum = 0

    while (i < input.length) {
        if (i + 2 < input.length &&
            input[i] == 'd' && input[i + 1] == 'z' && input[i + 2] == '=') {
            sum++
            i += 3
        } else if (
            (i + 1 < input.length) &&
            ((input[i] == 'c' && (input[i + 1] == '=' || input[i + 1] == '-')) ||
            (input[i] == 'd' && input[i + 1] == '-') ||
            (input[i] == 'l' && input[i + 1] == 'j') ||
            (input[i] == 'n' && input[i + 1] == 'j') ||
            (input[i] == 's' && input[i + 1] == '=') ||
            (input[i] == 'z' && input[i + 1] == '='))
            ) {
            sum++
            i += 2
        } else{
          sum++
          i++
        }
    }

    println(sum)
}