class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        current_color = image[sr][sc]



        def dfs(image, r, c, color, current_color):
            inbound_x = 0 <= r < len(image)
            inbound_y = 0 <= c < len(image[0])
            if not inbound_x or not inbound_y or image[r][c] == color or image[r][c] != current_color:
                return 

            image[r][c] = color

            dfs(image, r+1, c,color,  current_color)
            dfs(image, r-1, c,color ,current_color)
            dfs(image, r, c+1,color, current_color)
            dfs(image, r, c-1, color, current_color)
        
        dfs(image,sr,sc,color, current_color)

        return image

        