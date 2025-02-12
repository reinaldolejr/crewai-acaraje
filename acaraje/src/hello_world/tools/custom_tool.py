from crewai.tools import BaseTool
from typing import Type

from selenium import webdriver


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Internet search tool" # fica a vontade pra mudar o nome e assinatura, ou criar mais ferramentas
    description: str = (
        "This tool uses selenium to search for a term on the internet."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        print(f"Running MyCustomTool with argument {argument}")
        # Implementation goes here

        # use playwright to open google and search for acarajé, get text from the first result and return it
        # with sync_playwright() as p:
        #     browser = p.chromium.launch()
        #     page = browser.new_page()
        #     page.goto("https://www.google.com")
        #     page.fill("input[name=q]", "acarajé")
        #     page.keyboard.press("Enter")
        #     page.wait_for_selector("h3")
        #     result = page.query_selector("h3").inner_text()
        #     browser.close()

        # return result

        driver = webdriver.Chrome()

        # sugestão, pesquisa no google maps por acarajé
        driver.get("https://www.google.com/maps/search/acaraj%C3%A9")

        # processa o resultado antes de retornar.

        # não retorna a pagina toda porque tem muito token
        # return driver.page_source
        return "Acarajé can be found only in Salvador, Bahia, Brazil."


        # return "this is an example of a tool output, ignore it and move along."
