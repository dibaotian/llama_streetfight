this project is based on the https://github.com/OpenGenerativeAI/llm-colosseum


#### create a enviroment
#### $conda create -n  llm_streetfight python=3.8.10
#### To activate this environment, use
####     $ conda activate llm_streetfight
#### To deactivate an active environment, use
####     $ conda deactivate

1   In the ollama.py ， set the llama3 and llama2 as model

```python
game = Game(
        render=True,
        save_game=True,
        player_1=Player1(
            nickname="minxie",
            model="ollama:llama3",
            # model="ollama:mistral",
        ),
        player_2=Player2(
            nickname="xiemin",
            model="ollama:llama2",
            # model="ollama:mistral",
        ),
    )
```

2 in the llm.py register ollama client
```python
 elif provider == 'ollama':
        from llama_index.llms.ollama import Ollama # need install: pip install llama-index-llms-ollama
    
        return Ollama(model=model_name, request_timeout=90.0)
```

also need install the llama_index.llms.ollama mosule

pip install llama-index-llms-ollama

make local


