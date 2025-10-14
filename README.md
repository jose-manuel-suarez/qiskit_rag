# Proyecto Refactoring en Qiskit con RAG

### Data ingestion

   - Se toma desde el directorio /data-ingestion, inicialmente solo las notas de liberación.

### Modelo de Embeddings

   - Actualmente utilizamos ollama:nomic-embed-text:v1.5
  
### Etapas experimentales

   - Consideramos los siguientes modelos de prueba:
     - Ollama GPT-oss20B (local)
     - OpenAI ChatGPT-4.0 / ChatGPT-4.1
     - DeepSeek v3 (no sabemos si podremos probar desde n8n)
     - Google Gemini Flash-2.5 

### Parametrizaciones

| Parámetro |    | Descripción |
| :-------  | :- | :---------  |
| rag_chatbot_step || Indica si la ejecución utilizará el bot para procesamiento de snippets o sólo carga de la BBDD de embeddings. |
| is_restricted || Indica si el procesamiento incorpora o no a las notas de liberación Qiskit, la taxonomía automática de escenarios. |
| no_refactoring_chatbot_step || Indica si el prompt incorpora solicitud de código adaptado o sólo los escenarios detectados. |
| repo-github || Parametrizaciones asociados al repositorio remoto. |
| | owner | Propietario del repositorio GitHub experimental. |
| | name | Nombre del proyecto GitHub. |
| | data-ingestion-path | Directorio de ingesta de datos. |
| | data-rag-chatbot-path | Directorio de fuentes de datos para el modelo. |
| | snippets-path | Directorio de fragmentos de código python para pruebas. |
| | prompts-path | Directorio de solicitudes para el modelo (usuario y sistema). |
| | answers-path | Directorio de archivos resultantes para cada prueba. |
| target-repo-url | | Url base del repositorio web del proyecto. |
| target-version | | |
| only_qrn_for_data_ingestion | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| selected-ai-agent | | Indica el agente AI a utilizar (valores posibles: 'gemini' / 'ollama' / 'openai' ) |