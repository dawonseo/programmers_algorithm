def solution(brown, yellow):
    height = 3
    width = (brown - (height - 2) * 2) // 2
    
    while width >= height:
        if width * height - brown == yellow:
            return [width, height]
        else:
            height += 1
            width = (brown - (height - 2) * 2) // 2
        
