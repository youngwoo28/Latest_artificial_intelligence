import json

# 실제 날씨 API를 호출하는 대신, 샘플 데이터를 반환하는 함수
def get_current_weather(location, unit="celsius"):
    """
    지정된 위치의 현재 날씨 정보를 가져옵니다.
    실제로는 외부 날씨 API를 호출해야 하지만,
    여기서는 가짜 데이터를 반환하도록 시뮬레이션합니다.
    """
    weather_info = {
        "location": location,
        "temperature": 22,   # 단위는 기본적으로 섭씨
        "unit": unit,
        "forecast": "sunny"
    }
    return json.dumps(weather_info, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    result = get_current_weather("Seoul")
    print(result)