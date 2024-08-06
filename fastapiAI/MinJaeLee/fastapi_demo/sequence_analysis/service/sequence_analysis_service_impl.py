from sequence_analysis.repository.sequence_analysis_repository_impl import SequenceAnalysisRepositoryImpl
from sequence_analysis.service.sequence_analysis_service import SequenceAnalysisService


class SequenceAnalysisServiceImpl(SequenceAnalysisService):
    def __init__(self):
        self.sequenceAnalysisRepository = SequenceAnalysisRepositoryImpl()

    def predictNextSequence(self, userSendMessage):
        print(f"service -> predictNextSequence()")

        tokenizer = self.sequenceAnalysisRepository.createTokenizer(userSendMessage)
        totalWord, inputSequences = self.sequenceAnalysisRepository.extractSequence(tokenizer, userSendMessage)

        maxSequenceLength = max([len(x) for x in inputSequences])
        paddedInputSequences = self.sequenceAnalysisRepository.paddingSequence(inputSequences, maxSequenceLength)
        X, y = self.sequenceAnalysisRepository.separateInputAndOutputSequences(paddedInputSequences, totalWord)
        trainedModel = self.sequenceAnalysisRepository.trainSequence(totalWord, maxSequenceLength, X, y)

        generatedText = self.sequenceAnalysisRepository.generateText("비가 멈추지 않고", 3, trainedModel, maxSequenceLength, tokenizer)

        return generatedText
