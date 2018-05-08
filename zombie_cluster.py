"""
Zombie ClustersThere are zombies in Seattle. Liv and Ravi are trying to track
them down to find out who is creating new zombies in an effort
to prevent an apocalypse. Other than the patient-zero zombies
(who became so by mixing MaxRager and tainted Utopium),
new people only become zombies after being scratched by an
existing zombie. Zombiism is transitive. This means that if
zombie 0 knows zombie 1 and zombie 1 knows zombie 2, then
zombie 0 is connected to zombie 2 by way of knowing zombie
1. A zombie cluster is a group of zombies who are directly or
indirectly linked through the other zombies they know, such as
the one who scratched them or supplies who them with brains.
The diagram showing connectedness will be made up of a
number of binary strings, characters 0 or 1. Each of the
characters in the string represents whether the zombie
associated with a row element is connected to the zombie at
that character's index. For instance, a zombie 0 with a
connectedness string '110' is connected to zombies 0 (itself)
and zombie 1, but not to zombie 2. The complete matrix of
zombie connectedness is:
110
110
001
Zombies 0 and 1 are connected. Zombie 2 is not.
Your task is to determine the number of connected groups of
zombies, or clusters, in a given matrix.
Note: Method signatures may vary depending on the
requirements of your chosen language.
Function Description
Complete the function zombie_cluster in the editor below. The
function must return an integer representing the number of
zombie clusters counted.
zombie_cluster has the following parameter(s):
zombies[z 0 ,...z n-1 ]: an array of strings of binary digits
z i representing connectedness of zombies
Constraints
1 ≤ n ≤ 300
0 ≤ i < n
|zombies| = n
Each z i contains a binary string of n zeroes and ones. It is a
square matrix.
Input Format for Custom Testing
Sample Case 0Sample Input 0
4
1100
1110
0110
0001
Sample Output 0
2
In the diagram below, the squares highlighting a known
connection between two different zombies are highlighted in
green. Because each zombie is already aware that they are
personally a zombie, those are highlighted in grey.
Explanation 0
We have n = 4 zombies numbered z 0 through z 3 . There are 2
pairs of zombies who directly know each another: (z 0 , z 1 ) and
(z 1 , z 2 ). Because of zombiism's transitive property, the set of
zombies {z 0 , z 1 , z 2 } is considered to be a single zombie
cluster. The remaining zombie, z 3 , doesn't know any other
zombies and is considered to be his own, separate zombie
cluster ({z 3 }). This gives us a total of 2 zombie clusters.
"""


# zombie[i][j] = 1 means i and j know each other
# find the number of Zombie clusters(disjoint sets) 

def DFS(j, visited, zombies, row):
    for k in range(row):
        if zombies[j][k] == '1' and visited[j][k] == False and visited[k][j] == False:
            visited[j][k] = True
            visited[k][j] = True
            DFS(k,visited,zombies, row) 

def  zombie_cluster(zombies):
    row = len(zombies)
    col = len(zombies[0])
    count = 0
    if row == 0 or col == 0:
        return count
    visited = [[False for j in range(col)]for i in range(row)]
    for i in range(row):
        bol = False
        for j in range(row):
            if zombies[i][j] == '1' and visited[i][j] == False and visited[j][i] == False:
                visited[i][j] = True
                visited[j][i] = True
                DFS(j,visited,zombies, row) 
                if bol == False:
                    count += 1
                    bol = True
    return count

if __name__ == '__main__':
    n = int(input())
    zombies = [input() for _ in range(n)]
    print(zombie_cluster(zombies))