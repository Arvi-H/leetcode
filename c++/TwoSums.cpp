/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
*/

#include <iostream>
#include <vector>
#include <map>

using namespace std;

class TwoSums {
public:
    vector<int> twoSum (vector<int>& nums, int target) {
        map<int, int> twoSumMap;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i]; 

            if (twoSumMap.find(complement) != twoSumMap.end()) {
                return {twoSumMap[complement], i};  
            }

            twoSumMap[nums[i]] = i;  
        }
       
        return {};
    }
};
 
int main() {
    TwoSums twosums;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = twosums.twoSum(nums, target);
    
    cout << "Indices: [" << result[0] << ", " << result[1] << "]" << endl;
    
    return 0;
}


