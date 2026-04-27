package brute_force

data class Point(val x : Int, val y : Int)

fun main(){
    val N = readln().toInt()
    val curves = Array(N){
        readln().split(" ").map{ it.toInt() }
    }
    val points = mutableSetOf<Point>()

    for (c in curves){
        val result = makeCurve(Point(c[0],c[1]), c[2], c[3])
        points.addAll(result)
    }

    print(countSqu(points))
}

fun countSqu(points: Set<Point>): Int {
    var cnt = 0
    for (x in 0 until 100) {
        for (y in 0 until 100) {
            if (points.contains(Point(x, y)) &&
                points.contains(Point(x + 1, y)) &&
                points.contains(Point(x, y + 1)) &&
                points.contains(Point(x + 1, y + 1))
            ) {
                cnt++
            }
        }
    }
    return cnt
}

fun makeCurve(p: Point, d: Int, gen: Int): Set<Point> {
    val dx = intArrayOf(1, 0, -1, 0)
    val dy = intArrayOf(0, -1, 0, 1)

    val curvePoints = mutableListOf<Point>()

    curvePoints.add(p)
    curvePoints.add(Point(p.x + dx[d], p.y + dy[d]))

    for (i in 1..gen) {
        val pivot = curvePoints.last()

        for (j in curvePoints.size - 2 downTo 0) {
            val current = curvePoints[j]
            val nextX = pivot.x + (pivot.y - current.y)
            val nextY = pivot.y + (current.x - pivot.x)
            curvePoints.add(Point(nextX, nextY))
        }
    }
    return curvePoints.toSet()
}