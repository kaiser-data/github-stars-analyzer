# GitHub Stars Analyzer

A React web application that fetches and analyzes a user's GitHub starred repositories with comprehensive analytics, real-time trend analysis, and export capabilities.

## Features

- **Complete Data Fetching**: Retrieves all starred repositories (up to 1000) using GitHub API pagination
- **Recent Trend Analysis**: Real star history data for the last 30 days
  - Accurate counts (no approximations) using GitHub GraphQL API
  - Works for repos with 0 to 500k+ stars (no 40k limit!)
  - Trend classification: Hot 🔥, Rising ⚡, Steady ✨, Quiet 💤
  - Percentage growth display
  - Fast fetching (only last 30 days of data)
- **Comprehensive Analytics**:
  - Total repositories, stars, and average stars per repo
  - Top 5 programming languages by frequency
  - Top 10 most common topics with intelligent normalization
  - Semantic grouping (e.g., agent/ai-agent/agentic-ai → ai-agent, chatgpt/gpt/openai → openai)
  - Top 5 most-starred repositories
- **Advanced Sorting & Filtering**:
  - Sort by stars, forks, recent activity, or trends
  - Filter by programming language
  - Multi-select topic filtering (choose multiple topics from top 30)
  - Smart topic normalization to group related terms
  - View modes: All, Most Starred, Most Forked, Recently Updated
- **Flexible Layout Views**:
  - Grid view: 2-3 columns on widescreen
  - List view: Single column with full details
  - Compact view: 3-4 columns for maximum density
- **Detailed Repository View**: Cards showing all repo details with working links
  - Creation date and last updated date
  - Star count and fork count
  - Programming language and colorful glowing topic badges
  - Repository owner/author information
  - Top 5 contributors with avatars (on-demand loading)
- **Export Capabilities**: Download data as JSON or CSV
- **Rate Limit Handling**: Smart error messages and token authentication support
- **Responsive Design**: Works on desktop and mobile devices

## Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Usage

1. Enter a GitHub username
2. **Add a personal access token** (see below - required for trend analysis)
3. Click "Analyze Stars"
4. View analytics and repository list
5. Click "Show Recent Trends" on individual repos or "Load Trends for Top 20"
6. Export data using JSON or CSV buttons

## GitHub Token (Strongly Recommended)

**⚠️ A GitHub token is required for trend analysis features to work properly.**

### Why You Need a Token:
- **Without Token**: Limited to 60 requests/hour - insufficient for fetching star history
- **With Token**: 5,000 requests/hour - full access to all features including trend analysis

### How to Create a Token:

#### Option 1: Fine-Grained Personal Access Token (Recommended)
1. Go to: https://github.com/settings/tokens?type=beta
2. Click "Generate new token"
3. Add description: "GitHub Stars Analyzer"
4. Set expiration (e.g., 90 days)
5. Under "Repository access", select: "Public Repositories (read-only)"
6. Click "Generate token"
7. Copy the token (starts with `github_pat_`)
8. Paste into the application

#### Option 2: Classic Personal Access Token
1. Go to: https://github.com/settings/tokens/new
2. Add description: "GitHub Stars Analyzer"
3. Select scope: `public_repo` (read-only access)
4. Set expiration (e.g., 90 days)
5. Click "Generate token"
6. Copy the token (starts with `ghp_`)
7. Paste into the application

**Security Notes**:
- Token is only stored in browser session memory, never saved permanently
- The app only reads public repository data
- You can revoke the token anytime at: https://github.com/settings/tokens

## Tech Stack

- React 18 with Hooks
- Tailwind CSS for styling
- Lucide React for icons
- Vite for build tooling
- GitHub GraphQL API for trend analysis
- GitHub REST API v3 for repository data

## How Trend Analysis Works

The app uses GitHub's GraphQL API to fetch **accurate** star history data:

- **GraphQL Advantages**:
  - No 40k star limit (unlike REST API)
  - Fetches stars in DESC order (most recent first)
  - Accurate counts for any repository size (0 to 500k+ stars)

- **Optimization Strategy**:
  - Only fetches stars from the last 30 days
  - Early termination when reaching 30-day threshold
  - Fast performance (minimal API calls)
  - Real values (no approximations)

This approach provides accurate trend data while minimizing API calls and respecting rate limits.

## Data Collected

### Per Repository:
- **Basic info**: name, owner, description, URLs
- **Statistics**: total stars, forks, open issues
- **Metadata**: programming language, topics, license
- **Timestamps**: created date, last updated date, last push date
- **Trend Data** (when enabled):
  - Stars gained in last 30 days (accurate count)
  - Percentage growth relative to total stars
  - Trend classification (Hot 🔥/Rising ⚡/Steady ✨/Quiet 💤)

## Project Structure

```
github-stars-analyzer/
├── src/
│   ├── GitHubStarsAnalyzer.jsx  # Main component
│   ├── main.jsx                  # React entry point
│   └── index.css                 # Tailwind imports
├── index.html                    # HTML template
├── package.json                  # Dependencies
├── vite.config.js               # Vite configuration
├── tailwind.config.js           # Tailwind configuration
└── postcss.config.js            # PostCSS configuration
```

## Testing Suggestions

- Try "torvalds" for a user with many starred repos
- Try "sindresorhus" for repos with diverse languages and topics
- Test with your own GitHub username
- Click "Load Trends for Top 20" to see trend analysis in action
- Test individual "Show Recent Trends" buttons on different sized repos
- Verify export buttons download correctly (JSON and CSV)
- Check responsive layout on mobile devices
- Test sorting by different criteria (stars, trends, momentum)
- Test filtering by language and topic
- Test error handling with invalid usernames

## Browser Support

Modern browsers with ES6+ support:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Contributing

Contributions are welcome! Feel free to:
- Submit bug reports and feature requests
- Create pull requests with improvements
- Share your feedback and suggestions

For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

This project uses and is inspired by:
- **[GitHub REST API](https://docs.github.com/en/rest)** - For fetching starred repositories and repository data
- **[GitHub GraphQL API](https://docs.github.com/en/graphql)** - For accurate star history and trend analysis
- **[Star History](https://star-history.com/)** - Inspiration for visualizing repository star trends

Special thanks to the GitHub team for providing comprehensive APIs that make this project possible.

## License

MIT License

Copyright (c) 2024 Martin Kaiser

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact

Martin Kaiser - [martinkaiser.bln@gmail.com](mailto:martinkaiser.bln@gmail.com)

Project Link: [https://github.com/kaiser-data/github-stars-analyzer](https://github.com/kaiser-data/github-stars-analyzer)