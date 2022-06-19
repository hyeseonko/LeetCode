class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # method 1. Binary Search
        products.sort()
        output, prefix, index = [], "", 0
        for c in searchWord:
            prefix +=c
            index = bisect.bisect_left(products, prefix, index)
            output.append([product for product in products[index:index+3] if product.startswith(prefix)])
        
        return output
        