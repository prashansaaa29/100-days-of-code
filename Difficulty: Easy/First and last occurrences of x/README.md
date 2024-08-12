<h2><a href="https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x2041/1">First and last occurrences of x</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given an element <strong>x</strong> and a sorted array, <strong>arr[],</strong> find the&nbsp;</span><span style="font-size: 18.6667px;">indices</span><span style="font-size: 18.6667px;"> of </span><span style="font-size: 18.6667px;">first and last occurrences</span><span style="font-size: 14pt;"> of the </span><strong style="font-size: 14pt;">x</strong><span style="font-size: 14pt;">'s in the array.</span></p>
<p><span style="font-size: 14pt;">Note: If the number <strong>x </strong>is not found in the array, return '-1' as an array.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>x = 3, arr[] = [1, 3, 3, 4]
<strong>Output: </strong>[1, 2]
<strong>Explanation: </strong>For the above array, the first occurrence of X = 3 is at index = 1 and the last occurrence is at index = 2.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>x = 5, arr[] = [1, 2, 3, 4]
<strong>Output: </strong>[-1]
<strong>Explanation: </strong>As 5 is not present in the array, so the answer is -1.</span></pre>
<p><span style="font-size: 14pt;"><strong>Expected Time Complexity:</strong> O(logn)<br><strong>Expected Auxillary Space</strong><strong style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">:</strong><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;"> O(1)</span></span></p>
<p><span style="font-size: 14pt;"><strong>Constraints:&nbsp;</strong><br>1 &lt;= arr.size() &lt;= 10<sup>5</sup>&nbsp;<br>0 &lt;= arr[i], x &lt;= 10<sup>9</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Searching</code>&nbsp;<code>Binary Search</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;