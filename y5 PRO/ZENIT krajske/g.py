t = int(input())
for i in range(t):
    n,d,c = map(int,input().split())
    #ak c je vzdy mensie ako n
    #ak si odklada kazdy kilometer
    km_mapa = [n]+d*[0]
    for j,km in enumerate(km_mapa):

