from playwright.sync_api import sync_playwright

def auto_engage_linkedin_post(post_url, llm_generated_comment):
    """Navigates to a target prospect's post and drops an AI-generated contextual comment."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Assumes authenticated state is loaded via saved context
        context = browser.new_context(storage_state="linkedin_auth_state.json")
        page = context.new_page()
        
        try:
            page.goto(post_url)
            page.wait_for_selector("div.ql-editor") # Wait for comment box
            
            # Simulate human typing
            page.click("div.ql-editor")
            page.keyboard.type(llm_generated_comment, delay=150)
            
            # Click post (Commented out for safety in repo)
            # page.click("button.comments-comment-box__submit-button")
            print(f"Successfully staged engagement on {post_url}")
            
        except Exception as e:
            print(f"Engagement failed: {e}")
        finally:
            browser.close()
