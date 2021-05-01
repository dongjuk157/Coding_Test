import sys; input=sys.stdin.readline
N, M = map(int, input().split())
pokemon_dict = dict()
for i in range(1,N + 1):
    pokemon = input().rstrip()
    pokemon_dict[pokemon] = i
    pokemon_dict[str(i)] = pokemon
for _ in range(M):
    print(pokemon_dict[input().rstrip()])
