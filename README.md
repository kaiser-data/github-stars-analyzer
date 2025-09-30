# GitHub Stars Analyzer

A React web application that fetches and analyzes a user's GitHub starred repositories with comprehensive analytics and export capabilities.

## Features

- **Complete Data Fetching**: Retrieves all starred repositories (up to 1000) using GitHub API pagination
- **Comprehensive Analytics**:
  - Total repositories, stars, and average stars per repo
  - Top 5 programming languages by frequency
  - Top 10 most common topics
  - Top 5 most-starred repositories
- **Detailed Repository View**: Cards showing all repo details with working links
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
2. (Optional) Add a personal access token for higher rate limits
3. Click "Analyze Stars"
4. View analytics and repository list
5. Export data using JSON or CSV buttons

## GitHub Token

For best performance, create a personal access token:
1. Go to: https://github.com/settings/tokens/new
2. Add description: "Stars Analyzer"
3. Select scope: `public_repo` (read-only)
4. Generate and copy token
5. Paste into application

**Note**: Token is only stored in browser session, never permanently.

## Tech Stack

- React 18 with Hooks
- Tailwind CSS for styling
- Lucide React for icons
- Vite for build tooling
- GitHub REST API v3

## API Rate Limits

- **Without Token**: 60 requests/hour (~60 repos)
- **With Token**: 5000 requests/hour (all repos)

## Data Collected

Per repository:
- Basic info: name, owner, description, URLs
- Statistics: stars, forks, watchers, issues
- Metadata: language, topics, license
- Timestamps: created and updated dates

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

- Try "torvalds" for a user with many stars
- Test with your own GitHub username
- Verify export buttons download correctly
- Check responsive layout on mobile
- Test error handling with invalid usernames

## Browser Support

Modern browsers with ES6+ support:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## License

MIT