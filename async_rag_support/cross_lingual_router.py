from google.cloud import translate_v2 as translate

def route_multilingual_rag(user_query, target_language, rag_retriever_func):
    translate_client = translate.Client()
    
    # Step 1: Translate to English for optimal Vector DB search
    eng_query = translate_client.translate(user_query, target_language='en')['translatedText']
    
    # Step 2: Retrieve context
    context = rag_retriever_func(eng_query)
    
    # Step 3: Translate context back to user's native language
    localized_context = translate_client.translate(context, target_language=target_language)['translatedText']
    
    return localized_context
