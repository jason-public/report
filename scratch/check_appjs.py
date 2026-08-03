content = open('app.js', encoding='utf-8').read()
if 'switchView' in content:
    print("switchView: FOUND")
else:
    print("switchView: MISSING")

if 'renderTableView' in content:
    print("renderTableView: FOUND")
else:
    print("renderTableView: MISSING")
