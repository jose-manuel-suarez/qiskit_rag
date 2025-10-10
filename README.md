# Proyecto Refactoring en Qiskit con RAG

### Data ingestion

   - Se toma desde el directorio /data-ingestion, inicialmente solo las notas de liberación.

### Modelo de Embeddings

   - Actualmente utilizamos ollama:nomic-embed-text:v1.5

### Parametrizaciones

```python
[
{
"rag_chatbot_step": 
false,
"is_restricted": 
true,
"no_refactoring_chatbot_step": 
true,
"repo-github": 
{
"owner": 
"jose-manuel-suarez",
"name": 
"qiskit_rag",
"data-ingestion-path": 
"data-ingestion/",
"data-rag-chatbot-path": 
"data-rag-chatbot/",
"snippets-path": 
"data-rag-chatbot/snippets/",
"prompts-path": 
"data-rag-chatbot/prompts/",
"answers-path": 
"answers/"
},
"target-repo-url": 
"https://github.com/",
"target-version": 
"0.46.0",
"only_qrn_for_data_ingestion": 
true,
"user_prompt_file": 
"user_prompt.txt",
"system_prompt_file": 
"system_prompt.txt",
"chat-bot-model": 
"ollama-gpt-oss-20b"
}
]
```

| Parametro | Descripcion |
|  :-  | :-  |
| rag_chatbot_step | Indica si la ejecución utilizará el bot para procesamiento de snippets o sólo carga de la BBDD de embeddings. |