/*
    Given an integer n, return an array ans of length n + 1 
    such that for each i (0 <= i <= n), ans[i] is the number 
    of 1's in the binary representation of i.
*/

#include <iostream>
#include <vector>
#include <bitset>

using namespace std;

class CountingBits {
public:
    // O(n log(n))
    vector<int> countBits(int n) {
        vector<int> numOfBits (n+1);
        
        for (int i = 0; i <= n; i++) {
            // Convert int to binary
            string binaryRep = convert(i).to_string();
            int count = 0;

            // Count the number of 1's in the binary rep
            for (int j = 0; j < binaryRep.size(); j++) {
                if (binaryRep.at(j) == '1') {
                    count++;
                }
            }

            // Build vector
            numOfBits[i] = count;
        }

        return numOfBits;
    }

    bitset<8> convert(int n) {
        return bitset<8> (n);
    }

    // O(n) *** BEST SOLUTION ***
    vector<int> countBitsFaster(int n) {
        vector<int> count(n + 1);
        count[0] = 0;
        
        for (int i = 1; i <= n; i++) {
            count[i] = count[i / 2] + (i % 2);
        }

        return count;
    }
};


int main() {
    CountingBits cb;
    int n = 5;
    vector<int> bits = cb.countBits(n);
    for (int i = 0; i < bits.size(); i++) {
        cout << "Number of 1's in binary representation of " << i << " is " << bits[i] << endl;
    }
    return 0;
}