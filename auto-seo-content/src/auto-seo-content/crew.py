# crew.py
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

from dotenv import load_dotenv

# Carregando variáveis de ambiente
load_dotenv()

llm = LLM(model="gemini/gemini-2.0-flash")

@CrewBase
class SeoBlogPosts:
    """SEO Blog Posts Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    search_tool = SerperDevTool()

    llm = llm
    
    # --------------------------------------------------------------------------
    # Define Agents
    # --------------------------------------------------------------------------

    @agent
    def seo_keyword_finder(self) -> Agent:
        return Agent(
            config=self.agents_config["seo_keyword_finder"],
            verbose=True,
            tools=[self.search_tool],
            llm=self.llm
        )

    @agent
    def outline_creator(self) -> Agent:
        return Agent(
            config=self.agents_config["outline_creator"],
            verbose=True,
            llm=self.llm
        )

    @agent
    def content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["content_writer"],
            verbose=True,
            llm=self.llm
        )

    @agent
    def seo_checker(self) -> Agent:
        return Agent(
            config=self.agents_config["seo_checker"],
            verbose=True,
            llm=self.llm
        )

    @agent
    def link_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config["link_strategist"],
            verbose=True,
            tools=[self.search_tool],
            llm=self.llm
        )

    @agent
    def markdown_formatter(self) -> Agent:
        return Agent(
            config=self.agents_config["markdown_formatter"],
            verbose=True,
            llm=self.llm
        )

    # --------------------------------------------------------------------------
    # Define Tasks
    # --------------------------------------------------------------------------

    @task
    def keyword_research(self) -> Task:
        return Task(
            config=self.tasks_config["keyword_research"]
        )

    @task
    def create_outline(self) -> Task:
        return Task(
            config=self.tasks_config["create_outline"]
        )

    @task
    def draft_content(self) -> Task:
        return Task(
            config=self.tasks_config["draft_content"]
        )

    @task
    def optimize_seo(self) -> Task:
        return Task(
            config=self.tasks_config["optimize_seo"]
        )

    @task
    def link_strategy(self) -> Task:
        return Task(
            config=self.tasks_config["link_strategy"]
        )

    @task
    def format_markdown(self) -> Task:
        return Task(
            config=self.tasks_config["format_markdown"],
            output_file="blog_post.md"
        )

    # --------------------------------------------------------------------------
    # Define the Crew
    # --------------------------------------------------------------------------

    @crew
    def crew(self) -> Crew:
        
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
