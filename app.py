from github import Github
g=Github("basuswarnava2@gmail.com","SecurePass$2")
repos=g.search_repositories(query="language:javascript")
for repo in repos:
    print(repo)

for repo in g.get_user().get_repos():
    print(repo.name)

repo.startgazers_count

traff=repo.get_views_traffic()
traff

content=repo.get_contents("")
for content_file in content:
    print(content_file)