from crewai import Task


def create_research_tasks(
    topic,
    researcher,
    analyst,
    writer,
):
    research_task = Task(
        description=f"""
Research the topic:

{topic}

Requirements:

- Search the web thoroughly.
- Collect information from multiple trusted sources.
- Find at least 5 important facts.
- Mention recent developments.
- Include source URLs.
- Never invent facts.
""",
        expected_output="""
A complete research report containing:

- Topic
- Summary
- At least five facts
- Source URLs
""",
        agent=researcher,
    )

    analysis_task = Task(
        description="""
Analyze the research.

Tasks:

- Compare all findings
- Identify trends
- Detect conflicting information
- Evaluate source reliability
- Assign confidence (High / Medium / Low)
- Produce useful insights
""",
        expected_output="""
A detailed analysis containing:

- Key Insights
- Trends
- Confidence Level
- Observations
- Limitations
""",
        context=[research_task],
        agent=analyst,
    )

    report_task = Task(
        description="""
Create the final report.

Format:

# Executive Summary

# Key Findings

# Detailed Analysis

# Recommendations

# References

Requirements:

- Professional
- Well formatted
- Markdown
- Mention every source
""",
        expected_output="""
A professional Markdown report.
""",
        context=[research_task, analysis_task],
        agent=writer,
    )

    return [
        research_task,
        analysis_task,
        report_task,
    ]