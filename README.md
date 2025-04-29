# ollama-modelfiles

## Scope

## Usage

### PreSteps

0. Have [ollama][ollama] and python installed.

1. Run the version you want to use.
```bash
git clone https://github.com/jjasghar/ollama-modelfiles
cd ollama-modelfiles
cd <version you want>
ollama create $(pwd | cut -d / -f 8) -f Modelfile && ollama run $(pwd | cut -d / -f 8)
```


## License & Authors

If you would like to see the detailed LICENSE click [here](./LICENSE).

- Author: JJ Asghar <awesome@ibm.com>

```text
Copyright:: 2025- IBM, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

[ollama]: https://ollama.com
