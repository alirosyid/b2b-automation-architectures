export default {
  async fetch(request, env) {
    console.log("[Edge Router] Intercepting AI API request...");
    
    let response = await fetch("https://api.primary-llm.com/v1/chat", request);
    
    if (response.status === 429 || response.status >= 500) {
      console.log("[Edge Router] Primary LLM failed. Automatically routing to fallback API...");
      
      const fallbackRequest = new Request("https://api.fallback-llm.com/v1/chat", request);
      response = await fetch(fallbackRequest);
    }
    
    return response;
  }
};
