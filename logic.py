import random
weather, temp = input().split(",")
temp = int(temp)
def classify_temp(temp):
    if temp > 30:
        return "hot"
    elif 20 < temp <= 30:
        return "warm"
    elif 10 < temp <= 20:
        return "mild"
    elif 0 <= temp <= 10:
        return "chilly"
    else:
        return "freezing"
weather_food_map = {
    # 30도 초과
    ("hot", "비"): ["콩국수", "냉우동", "열무국수"],
    ("hot", "흐림"): ["냉면", "김밥", "쫄면"],
    ("hot", "맑음"): ["회덮밥", "비빔냉면", "샐러드"],
    ("hot", "눈"): ["밀면", "물냉면", "빙수"],

    # 20~30도
    ("warm", "비"): ["칼국수", "수제비", "부침개"],
    ("warm", "흐림"): ["비빔밥", "우동", "제육덮밥"],
    ("warm", "맑음"): ["냉모밀", "잔치국수", "김치볶음밥"],
    ("warm", "눈"): ["유부우동", "떡국", "매운라면"],

    # 10~20도
    ("mild", "비"): ["감자탕", "순두부찌개", "어묵탕"],
    ("mild", "흐림"): ["부대찌개", "된장찌개", "볶음우동"],
    ("mild", "맑음"): ["제육볶음", "쌈밥", "비빔국수"],
    ("mild", "눈"): ["샤브샤브", "온면", "계란찜"],

    # 0~10도
    ("chilly", "비"): ["김치찌개", "닭개장", "우거지해장국"],
    ("chilly", "흐림"): ["불고기", "보쌈", "해물순두부"],
    ("chilly", "맑음"): ["떡국", "순대국", "청국장"],
    ("chilly", "눈"): ["곰탕", "설렁탕", "국밥"],

    # 0도 미만
    ("freezing", "비"): ["얼큰이칼국수", "매운탕", "소고기무국"],
    ("freezing", "흐림"): ["돼지국밥", "감자탕", "김치찜"],
    ("freezing", "맑음"): ["갈비탕", "추어탕", "장어구이"],
    ("freezing", "눈"): ["전골", "생선조림", "닭한마리"]
}
status = classify_temp(temp)
print(random.choice(weather_food_map[(status,weather)]))

