class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        vector<vector<int>> v(nums.size() +1 , vector<int>());
        for(auto& it: nums){
            map[it]++;

        }

        for(auto it: map){
            v[it.second].push_back(it.first);
        }
        vector<int> ans;

        for(int i = nums.size(); i >=0 ; i--){
            for(auto it:v[i]){
                if(ans.size()==k){
                    break;
                }
                ans.push_back(it);
            }
        }

        return ans;

        
    }
};