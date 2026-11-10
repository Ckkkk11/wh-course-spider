import requests
import json


cookie_str = "JSESSIONID=534728EB370FFDD6A5885B2FB7984F8F; route=ec9f1523782f6fc8f64960f81492aa8e"

def get_course_table():
    url = "https://jw1.hustwenhua.net/jwglxt/kbcx/xskbcx_cxXsgrkb.html?gnmkdm=N253508"
    headers = {
        "Cookie": cookie_str,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36 Edg/157.0.0.0",
        "Referer": "https://jw1.hustwenhua.net/jwglxt/kbcx/xskbcx_cxXsgrkb.html?gnmkdm=N253508",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    form_data = {
        "xnm": "2026",
        "xqm": "3",
        "kzlx": "ck",
        "xsdm": "",
        "kclbdm": "",
        "kclxdm": ""
    }
    try:
        resp = requests.post(url, headers=headers, data=form_data, timeout=10)
        resp.encoding = "utf-8"
        res = resp.json()
        course_list = res.get("sjkList", [])
        return course_list
    except Exception as e:
        print(f"请求出错：{e}")
        return []


def week_num_to_cn(num):
    map_dict = {
        "1": "周一",
        "2": "周二",
        "3": "周三",
        "4": "周四",
        "5": "周五",
        "6": "周六",
        "7": "周日"
    }
    return map_dict.get(num, "未知")

if __name__ == "__main__":
    courses = get_course_table()
    print("=" * 60)
    print("📅 文华学院个人课表")
    print("=" * 60)
    print(f"一共获取 {len(courses)} 条课程记录\n")

    for course in courses:
        week_cn = week_num_to_cn(course.get("day"))
        course_name = course.get("kcmc")
        teacher = course.get("jsxm")
        info = course.get("qskcs")
        print(f"【{week_cn}】课程：{course_name} | 教师：{teacher} | 安排：{info}")