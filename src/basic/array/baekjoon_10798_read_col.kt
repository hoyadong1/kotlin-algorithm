package basic.array

fun main() {
    val lines = List(5) { readln() }
    val maxLen = lines.maxOf { it.length }

    for (col in 0..<maxLen) {
        for (row in 0..<5) {
            if (col < lines[row].length) print(lines[row][col])
        }
    }
}