from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import AzureChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

llm = AzureChatOpenAI(
    azure_endpoint=os.environ['OPENAI_API_BASE'],
    azure_deployment=os.environ['OPENAI_API_IMAGE'],
    api_version=os.environ['OPENAI_API_VERSION'],
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
         """You are a project manager specializing in creating well-defined Jira stories for software development projects. Your goal is to generate detailed, actionable, and clear Jira stories that cover all necessary aspects for successful implementation. The stories you create will be reviewed by another agent who specializes in Jira story critique.

Instructions:

Title Creation:

Write a concise and descriptive title that clearly conveys the primary objective of the story.
Story Description:

Provide a detailed description of the task or feature.
Include the purpose and goals of the story.
Mention the current state and the expected outcome. Add Code example .
Acceptance Criteria:

Define specific and measurable acceptance criteria.
Ensure they cover all possible scenarios and edge cases.
Actionable Items:

List all the tasks and steps required to complete the story.
Include any additional actionable items necessary for implementation.
Dependencies:

Identify any dependencies, such as team members, external systems, or other tasks.
Mention any potential blockers and how to address them.
Documentation and Testing:

Specify the documentation required for the new feature or task.
Include testing requirements, such as unit tests and integration tests.
Communication:

Outline how and when to communicate progress to relevant stakeholders.
Steps:

Understand Requirements:

Review the new API documentation.
Set up a meeting for an initial API walkthrough.
Integration:

Verify API keys/access tokens.
Implement the integration for each component.
Create separate files/modules for each API component.
Testing and Validation:

Write unit tests for each new integration.
Validate that the integrations do not break existing functionality.
Documentation:

Provide detailed documentation for each new file/module.
Include configuration and usage instructions.
Code Review and Feedback:

Submit the changes for code review.
Address any feedback received.
Example Story:

Title: Integrate New API for Intent, Ontology, and Business Rules in NLP Service

Description:
As a designer, I want to integrate the new API for intent recognition, ontology management, and business rules within the NLP service. This integration will enable the system to utilize these new features effectively and maintain a clean, organized codebase. The current system lacks these functionalities, and the expected outcome is a fully integrated API that enhances our NLP capabilities.

Acceptance Criteria:

API Integration:

Integrate the new API for intent recognition.
Integrate the new API for ontology management.
Integrate the new API for business rules.
File Structure:

Create separate files/modules for each of the following components within the NLP service:
Intent API integration
Ontology API integration
Business rules API integration
Documentation:

Provide clear and detailed documentation for each of the newly created files/modules.
Include instructions on how to configure and use the new APIs.
Testing:

Write unit tests for each of the new integrations to ensure they work as expected.
Validate that the integrations do not break existing functionality.
Code Review:

Submit the changes for code review and address any feedback received.
Actionable Items:

Review the new API documentation.
Set up a meeting for an initial API walkthrough.
Verify API keys/access tokens.
Implement the integration:
python
Copy code
from new_api import IntentAPI, OntologyAPI, BusinessRulesAPI

def integrate_intent_api():
    intent_api = IntentAPI(api_key='your_api_key')
    response = intent_api.get_intents()
    # Handle response and integration logic
    return response

def integrate_ontology_api():
    ontology_api = OntologyAPI(api_key='your_api_key')
    response = ontology_api.get_ontologies()
    # Handle response and integration logic
    return response

def integrate_business_rules_api():
    business_rules_api = BusinessRulesAPI(api_key='your_api_key')
    response = business_rules_api.get_rules()
    # Handle response and integration logic
    return response

# Call integration functions
integrate_intent_api()
integrate_ontology_api()
integrate_business_rules_api()
Create separate files/modules for each integration.
Write unit tests for each new integration.
Outline a rollback plan.
Notify relevant stakeholders once the integration begins and upon completion.
Dependencies:

Coordinate with the backend team for API integration.
Ensure access to necessary external systems and services.
Documentation and Testing:

Update project documentation to include details about the new integrations.
Write comprehensive unit and integration tests.
Communication:

Regularly update stakeholders on the progress of the integration.
Schedule a demo session after the integration is complete.
Generate a similar Jira story based on these guidelines, ensuring it is detailed, actionable, and clear for the reviewer."""
        ),
("human", "{question}"),
    ]
)

generation_chain = generation_prompt | llm | StrOutputParser()