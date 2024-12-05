import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")

# 将响应转化为字典
response_dict = r.json()
print(f"Total response: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# 仓库的信息
repo_dicts = response_dict['items']
print(f"Responsitories returned: {len(repo_dicts)}")
print(type(repo_dicts))
# 研究第一个仓库
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key,end=' ')
