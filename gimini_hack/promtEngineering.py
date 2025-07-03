from getUserInput import get_clipboard_text, get_file_text
import os

code_tamplate = """

include <stdio.h>
include <bits/stdc++.h>

define ll long long
define vi vector<int>
define vvi vector<vector<int>>
define vpii vector<pii>
define pb push_back
define pii pair<int, int>
define mii map<int, int>
define pqi priority_queue<int, vector<int>>
define pqig priority_queue<int, vector<int>, greater<int>>
define YES cout << "YES" << endl
define NO cout << "NO" << endl;
define srt sort(a.begin(), a.end())

using namespace std;

void solve()
{

}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t = 1;
    // cin>>t;
    while (t--)
        solve();
    return 0;
}
"""

track_problems = {}
last_clipboard_text = ""


def get_promt():

    # check if the clipboard has text
    getProblem = get_clipboard_text()
    if getProblem == last_clipboard_text:
        return ""

    promt = f"""write a cpp code using the following template:\n{code_tamplate}
        for the following problem: \n{getProblem}
        make sure to replace the solve function with the solution to the problem
    """

    return promt
