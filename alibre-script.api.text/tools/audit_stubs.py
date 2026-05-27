"""Audit Alibre Script stubs against the local API CSV and reflected output.

Run from `alibre-script.api.text`:

    python tools/audit_stubs.py

The script is intentionally read-only. It reports syntax validity, reflected
coverage against `alibre.script.api3.csv`, and duplicate overloaded method names
that cannot behave correctly in normal Python `.py` files.
"""

from __future__ import print_function

import ast
import csv
import os
import re
from collections import Counter, defaultdict


HERE = os.path.abspath(os.path.dirname(__file__))
API_TEXT_DIR = os.path.abspath(os.path.join(HERE, os.pardir))
WORKSPACE = os.path.abspath(os.path.join(API_TEXT_DIR, os.pardir))
STUB_DIR = os.path.join(WORKSPACE, "Alibre-Script-Stub-Files")
GENERATED_DIR = os.path.join(STUB_DIR, "generated")
GENERATED_PACKAGE_DIR = os.path.join(GENERATED_DIR, "package")
GENERATED_PACKAGE_MODULE_DIR = os.path.join(GENERATED_PACKAGE_DIR, "AlibreScript")
REFLECTED_OUTPUT_DIR = os.path.join(WORKSPACE, "Alibre-Script.Reflected", "output")
API_CSV = os.path.join(API_TEXT_DIR, "alibre.script.api2.csv")


STUB_FILES = [
    "alibre_script_api.py",
    "alibre_script_api_python27_docs.py",
    "alibre_script_api_docs.pyi",
    "alibre_script_api_advanced_docs.pyi",
    "AlibreScriptAPI_Mock.py",
    "mock_api.py",
    "mock_api (Original).py",
    "main.py",
]


def read_text(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def parse_check(path):
    try:
        ast.parse(read_text(path), filename=os.path.basename(path))
        return None
    except SyntaxError as exc:
        return exc


def api_method_arities():
    methods = defaultdict(set)
    method_re = re.compile(
        r"AlibreScript\.API\.([A-Za-z0-9_]+)\.([A-Za-z0-9_#]+)\((.*)\)"
    )
    with open(API_CSV, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            member = row.get("Member Name") or ""
            match = method_re.match(member)
            if not match:
                continue
            class_name, method_name, args = match.groups()
            if method_name == "#ctor":
                continue
            args = args.strip()
            arity = 0 if not args else len([a for a in args.split(",") if a.strip()])
            methods[(class_name, method_name)].add(arity)
    return methods


def reflected_method_arities():
    methods = defaultdict(lambda: defaultdict(set))
    duplicates = []

    if not os.path.isdir(REFLECTED_OUTPUT_DIR):
        return methods, duplicates

    for name in sorted(os.listdir(REFLECTED_OUTPUT_DIR)):
        if not name.endswith(".py"):
            continue
        path = os.path.join(REFLECTED_OUTPUT_DIR, name)
        error = parse_check(path)
        if error:
            duplicates.append((name, "<parse-error>", 0))
            continue
        tree = ast.parse(read_text(path), filename=name)
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            seen = []
            for item in node.body:
                if not isinstance(item, ast.FunctionDef):
                    continue
                arity = len(item.args.args)
                if arity and item.args.args[0].arg == "self":
                    arity -= 1
                methods[node.name][item.name].add(arity)
                seen.append(item.name)
            for method_name, count in Counter(seen).items():
                if count > 1:
                    duplicates.append((node.name, method_name, count))
    return methods, duplicates


def pyi_method_arities(path):
    methods = defaultdict(lambda: defaultdict(set))
    duplicate_without_overload = []
    if not os.path.exists(path):
        return methods, duplicate_without_overload, "missing"
    error = parse_check(path)
    if error:
        return methods, duplicate_without_overload, "line {0}: {1}".format(error.lineno, error.msg)
    tree = ast.parse(read_text(path), filename=os.path.basename(path))
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        seen = defaultdict(list)
        for item in node.body:
            if not isinstance(item, ast.FunctionDef):
                continue
            method_name = "#ctor" if item.name == "__init__" else item.name
            arity = len(item.args.args)
            if arity and item.args.args[0].arg == "self":
                arity -= 1
            methods[node.name][method_name].add(arity)
            seen[item.name].append(item)
        for method_name, items in seen.items():
            if len(items) <= 1:
                continue
            for item in items:
                has_overload = any(
                    isinstance(decorator, ast.Name) and decorator.id == "overload"
                    for decorator in item.decorator_list
                )
                if not has_overload:
                    duplicate_without_overload.append((node.name, method_name, len(items)))
                    break
    return methods, duplicate_without_overload, None


def runtime_duplicate_methods(path):
    duplicates = []
    if not os.path.exists(path):
        return duplicates, "missing"
    error = parse_check(path)
    if error:
        return duplicates, "line {0}: {1}".format(error.lineno, error.msg)
    tree = ast.parse(read_text(path), filename=os.path.basename(path))
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        names = [
            item.name for item in node.body if isinstance(item, ast.FunctionDef)
        ]
        for method_name, count in Counter(names).items():
            if count > 1:
                duplicates.append((node.name, method_name, count))
    return duplicates, None


def bad_dot_parameter_lines(path):
    bad = []
    pattern = re.compile(
        r"def [A-Za-z0-9_]+\([^)]*\b[A-Za-z_][A-Za-z0-9_]*\.[A-Za-z_][A-Za-z0-9_.]*"
    )
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for lineno, line in enumerate(f, 1):
            if pattern.search(line):
                bad.append(lineno)
    return bad


def main():
    print("Workspace:", WORKSPACE)
    print("API CSV:", API_CSV)
    print("")

    print("Generated stub check")
    generated_py = os.path.join(GENERATED_DIR, "AlibreScript.py")
    generated_pyi = os.path.join(GENERATED_DIR, "AlibreScript.pyi")
    package_init_py = os.path.join(GENERATED_PACKAGE_MODULE_DIR, "__init__.py")
    package_init_pyi = os.path.join(GENERATED_PACKAGE_MODULE_DIR, "__init__.pyi")
    package_setup = os.path.join(GENERATED_PACKAGE_DIR, "setup.py")
    for path in [generated_py, generated_pyi, package_init_py, package_init_pyi, package_setup]:
        name = os.path.relpath(path, STUB_DIR)
        error = parse_check(path) if os.path.exists(path) else "missing"
        if error is None:
            print("OK     {0}".format(name))
        elif error == "missing":
            print("MISSING {0}".format(name))
        else:
            print("FAIL   {0}: line {1}: {2}".format(name, error.lineno, error.msg))

    runtime_dups, runtime_error = runtime_duplicate_methods(generated_py)
    if runtime_error:
        print("Runtime duplicate check skipped:", runtime_error)
    else:
        print("Runtime duplicate method groups:", len(runtime_dups))
        if runtime_dups:
            print("First runtime duplicates:", runtime_dups[:10])

    package_runtime_dups, package_runtime_error = runtime_duplicate_methods(package_init_py)
    if package_runtime_error:
        print("Package runtime duplicate check skipped:", package_runtime_error)
    else:
        print("Package runtime duplicate method groups:", len(package_runtime_dups))
        if package_runtime_dups:
            print("First package runtime duplicates:", package_runtime_dups[:10])

    api = api_method_arities()
    generated_methods, pyi_dups, pyi_error = pyi_method_arities(generated_pyi)
    if pyi_error:
        print("Generated pyi coverage skipped:", pyi_error)
    else:
        missing_generated = []
        mismatched_generated = []
        for (class_name, method_name), arities in sorted(api.items()):
            generated_arities = generated_methods.get(class_name, {}).get(method_name)
            if not generated_arities:
                missing_generated.append((class_name, method_name, sorted(arities)))
            elif not (arities & generated_arities):
                mismatched_generated.append(
                    (class_name, method_name, sorted(arities), sorted(generated_arities))
                )
        print("Generated pyi duplicate methods without @overload:", len(pyi_dups))
        print("Generated pyi missing method groups:", len(missing_generated))
        print("Generated pyi arity mismatches:", len(mismatched_generated))
        if missing_generated:
            print("First generated missing:", missing_generated[:10])
        if mismatched_generated:
            print("First generated mismatches:", mismatched_generated[:10])

    print("")

    print("Stub syntax check")
    for name in STUB_FILES:
        path = os.path.join(STUB_DIR, name)
        if not os.path.exists(path):
            print("MISSING", name)
            continue
        error = parse_check(path)
        if error:
            print("FAIL   {0}: line {1}: {2}".format(name, error.lineno, error.msg))
        else:
            print("OK     {0}".format(name))

    print("")
    print("Invalid .NET-style parameter names")
    for name in STUB_FILES:
        path = os.path.join(STUB_DIR, name)
        if not os.path.exists(path):
            continue
        bad = bad_dot_parameter_lines(path)
        if bad:
            print(
                "{0}: {1} bad def lines; first {2}".format(
                    name, len(bad), ", ".join(str(x) for x in bad[:8])
                )
            )

    reflected, duplicates = reflected_method_arities()

    missing = []
    mismatched = []
    for (class_name, method_name), arities in sorted(api.items()):
        reflected_arities = reflected.get(class_name, {}).get(method_name)
        if not reflected_arities:
            missing.append((class_name, method_name, sorted(arities)))
        elif not (arities & reflected_arities):
            mismatched.append(
                (class_name, method_name, sorted(arities), sorted(reflected_arities))
            )

    print("")
    print("Reflected output coverage against API CSV")
    print("API method groups:", len(api))
    print("Missing method groups:", len(missing))
    print("Arity mismatches:", len(mismatched))
    if missing:
        print("First missing:", missing[:10])
    if mismatched:
        print("First mismatches:", mismatched[:10])

    print("")
    print("Duplicate overloaded method names in reflected .py files")
    print("Duplicate groups:", len(duplicates))
    for class_name, method_name, count in duplicates[:40]:
        print("{0}.{1}: {2} defs".format(class_name, method_name, count))
    if len(duplicates) > 40:
        print("... {0} more".format(len(duplicates) - 40))


if __name__ == "__main__":
    main()
