class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image == None or image[sr][sc] == newColor:
            return image
        
        self.flood(image, sr, sc, image[sr][sc], newColor)
        return image
              
    def flood(self, image, sr, sc, originalColor, newColor):
        
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != originalColor:
            return
        
        image[sr][sc] = newColor        
        self.flood(image,sr, sc+1, originalColor, newColor)
        self.flood(image,sr, sc-1, originalColor, newColor)
        self.flood(image,sr+1, sc, originalColor, newColor)
        self.flood(image,sr-1, sc, originalColor, newColor)