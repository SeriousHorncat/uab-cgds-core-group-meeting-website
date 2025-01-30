"""
Python script to generate HTML for a collaborative codespaces workshop session
"""

import os

from team import demo

generated_list = [
    getattr(demo, method)()
    for method in dir(demo)
    if not method.startswith("__") and "James" not in method
]

CSS = """
<style>

body {
  --wp--preset--font-size--small: 13px;
  --wp--preset--font-size--medium: 20px;
  --wp--preset--font-size--large: 36px;
  --wp--preset--font-size--x-large: 42px;
  --wp--preset--font-size--normal: 16px;
  --wp--preset--font-size--huge: 42px;
  --wp--preset--color--vivid-green-cyan: #00d068;

  line-height: 1.6842;
}

dt a {
  font-weight: 600;
}

dl {
  margin-bottom: 1.6842em;
}

dl a {
  text-decoration: none;
  color: black
}

dl a:visited {
  color: black;
}

.row {
  margin-right: -15px;
  margin-left: -15px;
  padding-right: 15px;
  padding-left: 15px;
}


#profiles {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
}
.profile {
    border: 1px solid #ccc;
    padding: 10px;
    text-align: center;
}
.profile img {
    max-width: 100px;
    border-radius: 90%;
}
</style>
"""

GENERATED_HTML = "\n".join(generated_list)

HTML = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Collaborative HTML Page</title>
    <style>
      {CSS}
    </style>

</head>
<body>
    <h1>All work and no play makes CGDS a dull lab - allegedly</h1>
    <div id="profiles">
      {GENERATED_HTML}
    </div>
</body>
</html>
"""

with open(
    "team.html",
    mode="w",
    encoding="utf-8",
) as file:
    file.write(HTML)

output_absolute_filepath = os.path.abspath("team.html")

amount = len(generated_list)
print(
    f"HTML file 'team.html' has been generated with {amount} publications in {output_absolute_filepath}"
)
