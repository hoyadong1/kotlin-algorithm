package dp

import java.util.PriorityQueue

data class Edge(val to: Int, val cost: Int, val time: Int)

data class Node(val idx: Int, val time: Int, val cost: Int) : Comparable<Node> {
    override fun compareTo(other: Node): Int = this.time - other.time
}

const val INF = 1_000_000_000

fun main() {
    val t = readln().toInt()
    val (n, m, k) = readln().split(" ").map{ it.toInt() }

    val adj = Array(n + 1) { mutableListOf<Edge>() }
    repeat(k) {
        val (u, v, c, d) = readln().split(" ").map{ it.toInt() }
        adj[u].add(Edge(v, c, d))
    }

    for (i in 1..n) {
        adj[i].sortBy { it.time }
    }

    val dp = Array(n + 1) { IntArray(m + 1) { INF } }
    val pq = PriorityQueue<Node>()

    dp[1][0] = 0
    pq.add(Node(1, 0, 0))

    var result = INF

    while (pq.isNotEmpty()) {
        val (curr, currTime, currCost) = pq.poll()

        if (currTime > dp[curr][currCost]) continue

        if (curr == n) {
            result = currTime
            break
        }

        for (edge in adj[curr]) {
            val nextCost = currCost + edge.cost
            val nextTime = currTime + edge.time

            if (nextCost <= m && dp[edge.to][nextCost] > nextTime) {
                for (i in nextCost..m) {
                    if (dp[edge.to][i] > nextTime) dp[edge.to][i] = nextTime
                    else break
                }
                pq.add(Node(edge.to, nextTime, nextCost))
            }
        }
    }

    if (result == INF) println("Poor KCM")
    else println(result)
}