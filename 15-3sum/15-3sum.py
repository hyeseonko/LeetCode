class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # three groups: p_group, n_group, z_group
        p_group, n_group, z_group = [], [], []
        for num in nums:
            if num>0:
                p_group.append(num)
            elif num<0:
                n_group.append(num)
            else:
                z_group.append(num)
        
        output = set()
        p_set, n_set = set(p_group), set(n_group)

        # case 1. [0,0,0]
        if len(z_group)>=3:
            output.add((0,0,0))
        
        # case 2. [0, p, -p]
        if len(z_group)>=1:
            for p in p_set:
                if -1*p in n_set:
                    output.add((0,p,-1*p))
        
        # case 3. [p1, p2, -(p1+p2)]
        for i in range(len(p_group)-1):
            for j in range(i+1, len(p_group)):
                if -1*(p_group[i]+p_group[j]) in n_set:
                    output.add(tuple(sorted([p_group[i], p_group[j], -1*(p_group[i]+p_group[j])])))
        
        # case 4. [n1, n2, -(n1+n2)]
        for i in range(len(n_group)-1):
            for j in range(i+1, len(n_group)):
                if -1*(n_group[i]+n_group[j]) in p_set:
                    output.add(tuple(sorted((n_group[i], n_group[j], -1*(n_group[i]+n_group[j])))))

        return output