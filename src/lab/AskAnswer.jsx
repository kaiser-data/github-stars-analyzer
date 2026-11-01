import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { MD_COMPONENTS } from './markdownComponents';

// Ask AI answers are Markdown (headings, tables, bold). Render them with the same
// components as the reports instead of as raw text. Lazy-loaded from LabApp so the
// markdown chunk is only fetched once an answer exists.
export default function AskAnswer({ text, streaming }) {
  return (
    <div className="text-sm">
      <ReactMarkdown remarkPlugins={[remarkGfm]} components={MD_COMPONENTS}>{text}</ReactMarkdown>
      {streaming && <span className="inline-block w-1.5 h-4 ml-0.5 -mb-0.5 bg-blue-400 animate-pulse" />}
    </div>
  );
}
