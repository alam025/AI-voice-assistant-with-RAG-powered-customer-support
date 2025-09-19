# 🤝 Contributing to AI Voice Assistant

Thank you for your interest in contributing to our AI Voice Assistant project! We welcome contributions from the voice technology and AI community and are grateful for your help in making this project better.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)
- [Voice Technology Guidelines](#voice-technology-guidelines)

## 📜 Code of Conduct

This project adheres to a Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git and GitHub account
- API accounts: OpenAI, Twilio, ElevenLabs, ngrok
- Basic understanding of voice processing, AI, and real-time systems
- Familiarity with FastAPI, async programming, and voice APIs

### Development Environment Setup

1. **Fork the repository**
   ```bash
   # Navigate to https://github.com/alam025/ai-voice-assistant
   # Click the "Fork" button
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-voice-assistant.git
   cd ai-voice-assistant
   ```

3. **Set up upstream remote**
   ```bash
   git remote add upstream https://github.com/alam025/ai-voice-assistant.git
   ```

4. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e .  # Install in development mode
   ```

6. **Setup environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

## 🛠️ How to Contribute

### Types of Contributions

We welcome several types of contributions:

- 🎙️ **Voice Processing Improvements**: Speech recognition, audio processing
- 🤖 **AI Integration Enhancements**: GPT models, RAG systems, conversation management
- 📞 **Communication Features**: Twilio integration, call handling, telephony
- 🏗️ **Architecture Improvements**: Performance, scalability, monitoring
- 📚 **Documentation**: API docs, tutorials, deployment guides
- 🧪 **Testing**: Voice processing tests, AI model validation, integration tests
- 🔧 **DevOps**: Deployment scripts, Docker, monitoring, CI/CD

### Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/voice-enhancement
   # or
   git checkout -b feature/ai-improvement
   # or
   git checkout -b feature/performance-optimization
   ```

2. **Make your changes**
   - Follow our coding standards
   - Add tests for voice processing and AI features
   - Update documentation as needed
   - Test with real voice calls if applicable

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: improve speech recognition accuracy with noise filtering"
   ```

4. **Push to your fork**
   ```bash
   git push origin feature/voice-enhancement
   ```

5. **Submit a Pull Request**

## 🏗️ Development Setup

### Project Structure Understanding

```
src/
├── main.py                     # FastAPI application server
├── assistant.py                # Main conversation handler
├── gpt_integration.py          # OpenAI GPT integration
├── voice_processing.py         # Speech recognition module
├── tts_synthesis.py           # Text-to-speech synthesis
└── utils/                     # Utility modules
    ├── audio_processing.py    # Audio manipulation
    ├── conversation_memory.py # Context management
    ├── rag_integration.py     # RAG knowledge retrieval
    └── error_handling.py      # Error management
config/
├── settings.py               # Application settings
├── logging.conf             # Logging configuration
└── api_config.py            # API configurations
tests/
├── test_voice_processing.py # Voice processing tests
├── test_gpt_integration.py  # AI integration tests
└── test_api_endpoints.py    # API endpoint tests
```

### Running Tests

```bash
# Run all tests
pytest

# Run voice processing tests
pytest tests/test_voice_processing.py

# Run AI integration tests
pytest tests/test_gpt_integration.py

# Run with coverage
pytest --cov=src

# Run integration tests (requires API keys)
pytest tests/integration/ --api-keys
```

### Testing Voice Features

```bash
# Test speech recognition
python scripts/test_speech.py

# Test voice synthesis
python scripts/test_tts.py

# Test full voice call flow
python scripts/test_call.py
```

## 📏 Coding Standards

### Python Style Guide

- **PEP 8 compliance**: Use `black` and `flake8`
- **Type hints**: Add type annotations for all functions
- **Docstrings**: Use Google-style docstrings with voice-specific examples
- **Async/await**: Use async programming for voice processing
- **Error handling**: Comprehensive error handling for voice and AI operations

### Code Formatting

```bash
# Format code with black
black src/ tests/

# Check linting
flake8 src/ tests/

# Type checking
mypy src/
```

### Example Code Style

```python
import asyncio
from typing import Dict, Any, Optional
from src.utils.error_handling import handle_voice_error

async def process_voice_input(
    audio_url: str,
    conversation_id: str,
    use_noise_reduction: bool = True
) -> Dict[str, Any]:
    """
    Process voice input with advanced speech recognition.
    
    Args:
        audio_url: URL to the audio recording
        conversation_id: Unique conversation identifier
        use_noise_reduction: Whether to apply noise reduction
        
    Returns:
        Dict containing transcription and confidence metrics
        
    Raises:
        VoiceProcessingError: If speech recognition fails
        AudioDownloadError: If audio download fails
        
    Example:
        >>> result = await process_voice_input(
        ...     "https://api.twilio.com/recording.wav",
        ...     "conv_123",
        ...     use_noise_reduction=True
        ... )
        >>> print(result['transcription'])
        "Hello, I need help with my account"
    """
    try:
        # Implementation with proper error handling
        pass
    except Exception as e:
        return handle_voice_error(e, conversation_id)
```

## 🧪 Testing Guidelines

### Voice Processing Tests

```python
import pytest
from unittest.mock import patch, MagicMock
from src.voice_processing import AdvancedVoiceProcessor

class TestVoiceProcessing:
    @pytest.fixture
    def voice_processor(self):
        return AdvancedVoiceProcessor()
    
    @patch('src.voice_processing.requests.get')
    def test_voice_transcription_accuracy(self, mock_get, voice_processor):
        """Test voice transcription with mock audio."""
        # Mock Twilio audio response
        mock_get.return_value.content = self.load_test_audio("test_voice.wav")
        mock_get.return_value.status_code = 200
        
        result = voice_processor.process_twilio_recording("test_url")
        
        assert result['transcription'] is not None
        assert result['confidence'] > 0.8
        assert 'quality_score' in result
    
    def test_noise_reduction_improves_accuracy(self, voice_processor):
        """Test that noise reduction improves recognition accuracy."""
        # Test with and without noise reduction
        noisy_audio = self.load_test_audio("noisy_voice.wav")
        
        result_without_nr = voice_processor.process_audio(noisy_audio, noise_reduction=False)
        result_with_nr = voice_processor.process_audio(noisy_audio, noise_reduction=True)
        
        assert result_with_nr['confidence'] > result_without_nr['confidence']
```

### AI Integration Tests

```python
class TestGPTIntegration:
    @pytest.fixture
    def gpt_manager(self):
        return EnterpriseGPTManager()
    
    @patch('src.gpt_integration.OpenAI')
    def test_contextual_response_generation(self, mock_openai, gpt_manager):
        """Test AI response generation with conversation context."""
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "I can help you with that!"
        mock_openai.return_value.chat.completions.create.return_value = mock_response
        
        result = gpt_manager.generate_contextual_response(
            "I need help with my account",
            "conv_123"
        )
        
        assert result['response'] == "I can help you with that!"
        assert 'tokens_used' in result
        assert result['model'] == 'gpt-4-turbo-preview'
```

## 📝 Pull Request Process

### Before Submitting

- [ ] All tests pass locally
- [ ] Voice processing features tested with real audio
- [ ] AI responses tested for quality and relevance
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No merge conflicts with main branch

### PR Checklist

```markdown
## Pull Request Checklist

- [ ] **Voice Technology**
  - [ ] Speech recognition accuracy maintained/improved
  - [ ] Audio processing optimized for real-time use
  - [ ] Voice synthesis quality verified

- [ ] **AI Integration**
  - [ ] GPT responses tested for quality and relevance
  - [ ] RAG system functioning correctly
  - [ ] Conversation context preserved properly

- [ ] **Code Quality**
  - [ ] Follows PEP 8 and project style guide
  - [ ] Comprehensive type hints and docstrings
  - [ ] Async/await used appropriately for voice processing

- [ ] **Testing**
  - [ ] Voice processing tests pass
  - [ ] AI integration tests pass
  - [ ] Real voice call testing completed

- [ ] **Documentation**
  - [ ] API documentation updated
  - [ ] Voice technology usage documented
  - [ ] Configuration examples provided
```

### PR Template

```markdown
## Description
Brief description of voice/AI improvements and motivation.

## Type of Change
- [ ] Voice processing enhancement
- [ ] AI model integration
- [ ] Performance optimization
- [ ] Documentation update
- [ ] Bug fix

## Testing
- [ ] Tested with real voice calls
- [ ] AI responses validated for quality
- [ ] Performance benchmarks run

## Voice Technology Impact
Describe impact on speech recognition, voice synthesis, or call handling.

## AI Integration Changes
Describe changes to GPT integration, RAG system, or conversation management.

## Performance Impact
Describe impact on response times, accuracy, or resource usage.
```

## 🎙️ Voice Technology Guidelines

### Audio Quality Standards
- **Sample Rate**: 16kHz minimum, 48kHz preferred
- **Bit Depth**: 16-bit minimum
- **Format**: WAV preferred, MP3 acceptable
- **Duration**: Support 1-60 second recordings
- **Noise Floor**: -60dB or better

### Speech Recognition Standards
- **Accuracy**: Maintain >90% accuracy on clean audio
- **Latency**: <500ms for speech-to-text conversion
- **Languages**: Primary support for English, extensible for others
- **Noise Handling**: Robust performance in noisy environments

### Voice Synthesis Standards
- **Quality**: High-fidelity, natural-sounding speech
- **Latency**: <1 second for text-to-speech conversion
- **Consistency**: Consistent voice characteristics across sessions
- **Emotion**: Support for different tones and emotions

## 🤖 AI Integration Guidelines

### GPT Integration Standards
- **Response Quality**: Relevant, helpful, and contextually appropriate
- **Token Efficiency**: Optimize for cost-effective API usage
- **Context Management**: Maintain conversation context across turns
- **Error Handling**: Graceful degradation when AI services fail

### RAG System Standards
- **Relevance**: Retrieved context must be relevant to user queries
- **Accuracy**: Knowledge base information must be current and accurate
- **Performance**: Context retrieval <200ms for real-time conversations
- **Coverage**: Comprehensive knowledge base for customer support scenarios

## 🏆 Recognition

Contributors will be recognized in several ways:

- **README.md**: Listed in contributors section
- **Release Notes**: Mentioned in version releases
- **Issues**: Tagged as contributors in resolved voice/AI issues

### Contributor Levels

- **Bronze**: 1-3 merged PRs in voice/AI technology
- **Silver**: 4-10 merged PRs or significant technical contributions
- **Gold**: 10+ merged PRs or major voice/AI innovations

## 📞 Getting Help

- **Documentation**: Check voice technology and AI integration docs
- **Issues**: Search existing voice/AI related issues
- **Discussions**: Use GitHub Discussions for technical questions
- **Code Review**: Request review from voice/AI technology maintainers

## 🚀 Advanced Contribution Areas

### High-Impact Contributions

- **Multi-language Support**: Implement voice processing for additional languages
- **Advanced AI Models**: Integrate newer GPT models or alternative LLMs
- **Performance Optimization**: Improve voice processing speed and accuracy
- **Enterprise Features**: Add monitoring, analytics, and scaling capabilities

### Research and Innovation

- **Emotion Detection**: Add emotional intelligence to voice processing
- **Voice Biometrics**: Implement speaker identification and verification
- **Advanced RAG**: Improve knowledge retrieval with better embedding models
- **Real-time Learning**: Implement systems that learn from conversations

Thank you for contributing to the future of AI voice technology! 🎙️🤖