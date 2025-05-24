from app.services.summarizer import Summarizer

summarizer = Summarizer()

def test_summarizer():
    input_text = (
        "Machine learning enables computers to learn from data. "
        "It is widely used in many industries to predict trends and automate decisions."
    )
    output = summarizer.summarize(input_text)
    assert isinstance(output, str)
    assert len(output) > 10
