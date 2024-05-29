#include <set>
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::set<int> seen;

        for(int num:nums){
            if(seen.find(num) != seen.end()){
                return true;
            }

            seen.insert(num);
        }

        return false;

        

    }
};