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
true,
"is_restricted": 
false,
"no_refactoring_chatbot_step": 
false,
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
"1.0.0",
"only_qrn_for_data_ingestion": 
false,
"user_prompt_file": 
"user_prompt.md",
"system_prompt_file": 
"system_prompt_free_w_qrn_w_tax.md",
"chat-bot-model": 
"google-gemini-2.5-flash",
"database-knowledge-name": 
"Qdrant Vector Store",
"qdrant-collection": 
"rag_ddbb",
"taxonomy-filename": 
"tax_gpt_1.0.0.md",
"validation_stage": 
false,
"selected-ai-agent": 
"gemini"
}
]
```

| Parámetro | Descripción |
| :-------  | :---------  |
| rag_chatbot_step | Indica si la ejecución utilizará el bot para procesamiento de snippets o sólo carga de la BBDD de embeddings. |
| is_restricted | Indica si el procesamiento incorpora o no a las notas de liberación Qiskit, la taxonomía automática de escenarios. |
| no_refactoring_chatbot_step | Indica si el prompt incorpora solicitud de código adaptado o sólo los escenarios detectados. |
| owner | Propietario del repositorio GitHub experimental. |
| name | Nombre del proyecto GitHub. |