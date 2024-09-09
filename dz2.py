import sys
import requests
import re


def fetch_package_info(package_name):
    package_name = package_name.replace(" (", "")
    package_name = package_name.replace("!", "")
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Package '{package_name}' not found.")
        sys.exit(1)


def extract_dependencies(package_info):
    requires_dist = package_info.get("info", {}).get("requires_dist", [])
    if requires_dist is None:
        return []

    parsed_deps = []
    for dep in requires_dist:
        dep_name = dep.split(";")[0].strip()
        dep_name = re.split('[<=>]', dep_name)[0].strip()
        if dep_name:
            parsed_deps.append(dep_name)
    return parsed_deps


def build_dependency_graph(package_name, package_info, graph, visited):
    if package_name in visited:
        return
    visited.add(package_name)

    dependencies = extract_dependencies(package_info)
    for dep in dependencies:
        if dep not in visited:
            graph.append(f'"{package_name}" -> "{dep}";')
            try:
                dep_info = fetch_package_info(dep)
                build_dependency_graph(dep, dep_info, graph, visited)
            except SystemExit:
                continue


def main():
    if len(sys.argv) != 2:
        print("python main.py и название пакета > graph.dot")
        sys.exit(1)

    package_name = sys.argv[1]
    package_info = fetch_package_info(package_name)

    graph = []
    visited = set()

    graph.append(f'digraph "{package_name}_dependencies" {{')
    build_dependency_graph(package_name, package_info, graph, visited)
    graph.append("}")

    print("\n".join(graph))


if __name__ == "__main__":
    main()
