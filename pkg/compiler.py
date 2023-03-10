config = {
  "cpp": {
    "suffix": "cpp",
    "images": ["frolvlad/alpine-gxx"],
    "time_limit": 2000,
    "memory_limit": 256,
    "compile_command": "g++ -O2 -Wall {code}",
    "run_command": "./a.out < {data}",
  },
  "python": {
    "suffix": "py",
    "images": ["frolvlad/alpine-python3"],
    "time_limit": 3000,
    "memory_limit": 256,
    "compile_command": None,
    "run_command": "python3 {code} < {data}",
  },
  "java": {
    "suffix": "java",
    "images": ["adoptopenjdk/openjdk8"],
    "time_limit": 3000,
    "memory_limit": 256,
    "compile_command": "javac -encoding utf-8 {code}",
    "run_command": "java -cp / Main < {data}",
  },
  "javascript": {
    "suffix": "js",
    "images": ["node"],
    "time_limit": 3000,
    "memory_limit": 256,
    "compile_command": None,
    "run_command": "node /{code} < {data}",
  },
  "go": {
    "suffix": "go",
    "images": ["frolvlad/alpine-go"],
    "time_limit": 2000,
    "memory_limit": 256,
    "compile_command": "go build {code}",
    "run_command": "./{target} < {data}",
  },
}
