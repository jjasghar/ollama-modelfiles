# ollama-modelfiles

## Scope

## Usage

```bash
git clone https://github.com/jjasghar/ollama-modelfiles
cd ollama-modelfiles
cd <version you want>
ollama create $(pwd | cut -d / -f 8) -f Modelfile && ollama run $(pwd | cut -d / -f 8)
```
