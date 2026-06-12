user = {
    "name": "홍길동",
    "age": 55,
    "skills": ["Python", "Git"]
}
user["name"] = "스티브잡스"

print(user["name"],"은 나이가 ", user["age"], "먹었습니다.")

mart = {
    "apple":  1000, 
    "banana": 2500, 
    "orange": 1500}

mart["apple"] = 5000

print(mart.keys())
print(mart.values())
print(mart.items())

for fruit, price in mart.items():
    print(f"{fruit}의 가격은 {price}원입니다.")