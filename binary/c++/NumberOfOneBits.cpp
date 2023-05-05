/*
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
 
Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
*/

#include <stdint.h>
#include <iostream>

using namespace std;

class NumberOfOneBits {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;

        while (n) {
            count += n & 1; // increment count by 0 if the n bit is 0 and by 1 if the n bit is 1 (bitwise AND)
            n >>= 1; // delete from n one by one
        }

        return count;
    }
};

int main() {
    NumberOfOneBits nb;

    uint32_t n = 00000000000000000000000000001011;
    int result = nb.hammingWeight(n);   
    cout << result << endl;  // Output: 3
}