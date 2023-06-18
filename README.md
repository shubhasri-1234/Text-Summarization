# Text Extraction and Summarization using Transformer Model

This project utilizes a Transformer model to extract and summarize text from various sources, such as YouTube videos, blogs, and websites. The project includes a website that takes a URL as input and generates a summary based on the desired number of sentences.Own Transformer model creation is tried(transformer_summarization.ipynb).

This project also summarizes text using hugging face models like Pegasus,T5 and Bart(Pegasus,T5,BART.ipynb).

## Features

- Extracts and summarizes content from different types of sources, including YouTube videos, blogs, and websites.
- Uses a Transformer model to perform both extractive and abstractive summarization.
- Provides the flexibility to specify the desired number of sentences in the summary.

## Usage
1. Input a URL of the desired content into the website.
2. Specify the number of sentences you want in the summary.
3. Click on the "Summarize" button.
4. The website will process the input and generate a concise summary of the text.

## How it Works

The project utilizes a Transformer model, a deep learning architecture known for its exceptional performance in natural language processing tasks. Here's a brief overview of how the Transformer model works:

1. Encoding: The input text is preprocessed by tokenizing it into words or subwords and converting it into a sequence of numerical vectors. This step involves creating a vocabulary during pre-training.
2. Encoder: The preprocessed input text is passed through an encoder component of the Transformer model, which consists of multiple self-attention layers. Each self-attention layer generates a contextualized representation of each input token by attending to all previous layers.
3. Decoding: The decoder component of the Transformer model generates the summary. Similar to the encoder, the decoder also consists of multiple self-attention layers. In addition to self-attention, the decoder attends to the encoder output to incorporate information from the input text. The decoder generates a probability distribution over the possible output tokens for each position in the summary, selecting the token with the highest probability as the predicted output.
4. Post Processing: The final summary is post-processed by converting numerical vectors back into words or subwords. Special tokens, such as the mask token, are removed, and the summary is formatted for readability.

## ROUGE (Recall-Oriented Understudy for Gisting Evaluation)

ROUGE is a set of metrics commonly used in text summarization to evaluate the quality of generated summaries. It measures the overlap between words or n-grams (contiguous sequences of n words) in the generated summary and the reference summary.
By comparing the generated summary with the reference summary using ROUGE, we can assess the effectiveness of the Transformer model in capturing the important information and generating coherent summaries. The ROUGE scores provide quantitative measures of the summarization quality, helping us determine the performance of the model and compare different Transformer models.

We have compared the ROUGE score of three models, namely, Pegasus, T5 and BART.


## Pegasus
Pegasus is a transformer-based model for abstractive summarization. It utilizes a standard Transformer encoder-decoder architecture and is trained with extracted gap sentences. Pegasus generates coherent summaries and has been used for various summarization tasks.

## T5
T5 (Text-to-Text Transfer Transformer) is a language model based on the transformer architecture. It employs a text-to-text framework for pre-training, making it suitable for extractive and abstractive summarization tasks.

## BART
BART (Bidirectional and Auto-Regressive Transformers) is a sequence-to-sequence model based on the transformer architecture. It combines denoising autoencoder and sequence-to-sequence objectives. BART produces high-quality summaries that are robust to variations in input text.


