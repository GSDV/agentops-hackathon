filename = "report.md"

def output_report(ticker, sections):
    output = f"# {ticker} Stock Report"
    for i in range(len(sections)):
        section = sections[i]
        output += f"\n\n# {section['heading']}\n{section['content']}"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(output)