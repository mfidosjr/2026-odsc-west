# Uso: source workshop/env-gemini.sh  (chaves lidas do Keychain; nada é gravado em arquivo)
export OPENAI_API_KEY="$(security find-generic-password -s costa-gemini-api-key -w)"
export TAVILY_API_KEY="$(security find-generic-password -s tavily-api-key -w)"
export OPENAI_BASE_URL="https://generativelanguage.googleapis.com/v1beta/openai"
export OPENAI_MODEL="gemini-3.8-flash"
export MEM0_DEFAULT_LLM_MODEL="gemini-3.8-flash"
export MEM0_DEFAULT_EMBEDDER_MODEL="gemini-embedding-001"

# Exercícios: provedor externo compatível com OpenAI (Gemini)
export USE_OPENAI=false
export USE_EXTERNAL_AI=true
export EXTERNAL_LLM_URL="$OPENAI_BASE_URL"
export EXTERNAL_LLM_API_KEY="$OPENAI_API_KEY"
export EXTERNAL_LLM_MODEL="$OPENAI_MODEL"
