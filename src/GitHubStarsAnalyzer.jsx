import React, { useState } from 'react';
import {
  Star,
  GitFork,
  Eye,
  Calendar,
  ExternalLink,
  Download,
  AlertCircle,
  Github
} from 'lucide-react';

const GitHubStarsAnalyzer = () => {
  const [username, setUsername] = useState('');
  const [token, setToken] = useState('');
  const [repos, setRepos] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [summary, setSummary] = useState(null);

  const fetchStarredRepos = async () => {
    if (!username.trim()) {
      setError('Please enter a GitHub username.');
      return;
    }

    setLoading(true);
    setError('');
    setRepos([]);
    setSummary(null);

    try {
      let allRepos = [];
      let page = 1;
      const maxPages = 10;

      while (page <= maxPages) {
        const headers = {
          'Accept': 'application/vnd.github.v3+json'
        };

        if (token.trim()) {
          headers['Authorization'] = `token ${token}`;
        }

        const response = await fetch(
          `https://api.github.com/users/${username}/starred?per_page=100&page=${page}`,
          { headers }
        );

        if (response.status === 404) {
          setError('User not found. Please check the username.');
          setLoading(false);
          return;
        }

        if (response.status === 403) {
          const rateLimitReset = response.headers.get('X-RateLimit-Reset');
          const resetTime = rateLimitReset
            ? new Date(rateLimitReset * 1000).toLocaleTimeString()
            : 'unknown';
          setError(
            `Rate limit exceeded. Please add a GitHub personal access token. Rate limit resets at ${resetTime}.`
          );
          setLoading(false);
          return;
        }

        if (!response.ok) {
          throw new Error(`GitHub API error: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();

        if (data.length === 0) {
          break;
        }

        allRepos = [...allRepos, ...data];
        page++;
      }

      if (allRepos.length === 0) {
        setError('This user has no starred repositories.');
        setLoading(false);
        return;
      }

      const processedRepos = allRepos.map(repo => ({
        id: repo.id,
        name: repo.name,
        full_name: repo.full_name,
        owner: repo.owner.login,
        description: repo.description || 'No description',
        html_url: repo.html_url,
        homepage: repo.homepage,
        stargazers_count: repo.stargazers_count,
        forks_count: repo.forks_count,
        watchers_count: repo.watchers_count,
        open_issues_count: repo.open_issues_count,
        language: repo.language || 'Unknown',
        topics: repo.topics || [],
        license: repo.license?.name || 'No license',
        created_at: new Date(repo.created_at).toLocaleDateString(),
        updated_at: new Date(repo.updated_at).toLocaleDateString()
      }));

      setRepos(processedRepos);
      generateSummary(processedRepos);
    } catch (err) {
      setError(`Failed to fetch starred repositories: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const generateSummary = (reposData) => {
    const totalRepos = reposData.length;
    const totalStars = reposData.reduce((sum, repo) => sum + repo.stargazers_count, 0);
    const avgStars = Math.round(totalStars / totalRepos);

    const languageCounts = {};
    const topicCounts = {};

    reposData.forEach(repo => {
      if (repo.language !== 'Unknown') {
        languageCounts[repo.language] = (languageCounts[repo.language] || 0) + 1;
      }
      repo.topics.forEach(topic => {
        topicCounts[topic] = (topicCounts[topic] || 0) + 1;
      });
    });

    const topLanguages = Object.entries(languageCounts)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5)
      .map(([lang, count]) => ({ language: lang, count }));

    const topTopics = Object.entries(topicCounts)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10)
      .map(([topic, count]) => ({ topic, count }));

    const mostStarred = [...reposData]
      .sort((a, b) => b.stargazers_count - a.stargazers_count)
      .slice(0, 5);

    setSummary({
      totalRepos,
      totalStars,
      avgStars,
      topLanguages,
      topTopics,
      mostStarred
    });
  };

  const exportToJSON = () => {
    const data = JSON.stringify({ repos, summary }, null, 2);
    const blob = new Blob([data], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${username}-starred-repos.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const exportToCSV = () => {
    const headers = ['Name', 'Owner', 'Description', 'Stars', 'Forks', 'Language', 'URL', 'Updated'];
    const rows = repos.map(repo => [
      repo.name,
      repo.owner,
      `"${repo.description.replace(/"/g, '""')}"`,
      repo.stargazers_count,
      repo.forks_count,
      repo.language,
      repo.html_url,
      repo.updated_at
    ]);

    const csvContent = [
      headers.join(','),
      ...rows.map(row => row.join(','))
    ].join('\n');

    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${username}-starred-repos.csv`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-gray-800 text-white py-8 px-4">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center mb-4">
            <Github className="w-12 h-12 mr-3 text-blue-400" />
            <h1 className="text-4xl font-bold">GitHub Stars Analyzer</h1>
          </div>
          <p className="text-gray-300">Analyze and export your GitHub starred repositories</p>
        </div>

        {/* Input Section */}
        <div className="bg-gray-700 rounded-lg p-6 mb-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            <div>
              <label className="block text-sm font-medium mb-2">GitHub Username</label>
              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Enter username"
                className="w-full px-4 py-2 bg-gray-800 text-white rounded-lg border border-gray-600 focus:outline-none focus:border-blue-500"
                disabled={loading}
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-2">
                Personal Access Token (Optional)
              </label>
              <input
                type="password"
                value={token}
                onChange={(e) => setToken(e.target.value)}
                placeholder="ghp_xxxxxxxxxxxx"
                className="w-full px-4 py-2 bg-gray-800 text-white rounded-lg border border-gray-600 focus:outline-none focus:border-blue-500"
                disabled={loading}
              />
            </div>
          </div>
          <button
            onClick={fetchStarredRepos}
            disabled={loading}
            className="w-full md:w-auto px-6 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 disabled:cursor-not-allowed rounded-lg font-medium transition-colors"
          >
            {loading ? 'Analyzing...' : 'Analyze Stars'}
          </button>
        </div>

        {/* Info Box */}
        <div className="bg-blue-900 bg-opacity-30 border border-blue-500 rounded-lg p-4 mb-6">
          <div className="flex items-start">
            <AlertCircle className="w-5 h-5 mr-3 mt-0.5 flex-shrink-0 text-blue-400" />
            <div className="text-sm text-gray-300">
              <p className="font-medium text-white mb-1">Rate Limit Information</p>
              <p>
                GitHub API limits unauthenticated requests to 60 per hour. For better performance,
                <a
                  href="https://github.com/settings/tokens/new"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-400 hover:text-blue-300 underline ml-1"
                >
                  create a personal access token
                </a>
                {' '}with 'public_repo' scope.
              </p>
            </div>
          </div>
        </div>

        {/* Error Display */}
        {error && (
          <div className="bg-red-900 bg-opacity-30 border border-red-500 rounded-lg p-4 mb-6">
            <div className="flex items-start">
              <AlertCircle className="w-5 h-5 mr-3 mt-0.5 flex-shrink-0 text-red-400" />
              <p className="text-red-200">{error}</p>
            </div>
          </div>
        )}

        {/* Summary Section */}
        {summary && (
          <div className="mb-8">
            {/* Stat Cards */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
              <div className="bg-gray-700 rounded-lg p-6">
                <h3 className="text-gray-400 text-sm font-medium mb-2">Total Repositories</h3>
                <p className="text-4xl font-bold">{summary.totalRepos.toLocaleString()}</p>
              </div>
              <div className="bg-gray-700 rounded-lg p-6">
                <h3 className="text-gray-400 text-sm font-medium mb-2">Total Stars</h3>
                <p className="text-4xl font-bold">{summary.totalStars.toLocaleString()}</p>
              </div>
              <div className="bg-gray-700 rounded-lg p-6">
                <h3 className="text-gray-400 text-sm font-medium mb-2">Average Stars/Repo</h3>
                <p className="text-4xl font-bold">{summary.avgStars.toLocaleString()}</p>
              </div>
            </div>

            {/* Analytics Section */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
              {/* Top Languages */}
              <div className="bg-gray-700 rounded-lg p-6">
                <h3 className="text-xl font-bold mb-4">Top Languages</h3>
                {summary.topLanguages.length > 0 ? (
                  <ul className="space-y-2">
                    {summary.topLanguages.map((lang, index) => (
                      <li key={lang.language} className="flex justify-between items-center">
                        <span className="text-gray-300">
                          {index + 1}. {lang.language}
                        </span>
                        <span className="text-gray-400">{lang.count} repos</span>
                      </li>
                    ))}
                  </ul>
                ) : (
                  <p className="text-gray-400">No language data available</p>
                )}
              </div>

              {/* Popular Topics */}
              <div className="bg-gray-700 rounded-lg p-6">
                <h3 className="text-xl font-bold mb-4">Popular Topics</h3>
                {summary.topTopics.length > 0 ? (
                  <div className="flex flex-wrap gap-2">
                    {summary.topTopics.map(topic => (
                      <span
                        key={topic.topic}
                        className="px-3 py-1 bg-blue-600 bg-opacity-30 border border-blue-500 rounded-full text-sm"
                      >
                        {topic.topic} ({topic.count})
                      </span>
                    ))}
                  </div>
                ) : (
                  <p className="text-gray-400">No topics data available</p>
                )}
              </div>
            </div>

            {/* Export Buttons */}
            <div className="flex gap-4 mb-6">
              <button
                onClick={exportToJSON}
                className="flex items-center px-4 py-2 bg-green-600 hover:bg-green-700 rounded-lg font-medium transition-colors"
              >
                <Download className="w-4 h-4 mr-2" />
                Export JSON
              </button>
              <button
                onClick={exportToCSV}
                className="flex items-center px-4 py-2 bg-green-600 hover:bg-green-700 rounded-lg font-medium transition-colors"
              >
                <Download className="w-4 h-4 mr-2" />
                Export CSV
              </button>
            </div>
          </div>
        )}

        {/* Repository List */}
        {repos.length > 0 && (
          <div>
            <h2 className="text-2xl font-bold mb-4">
              All Repositories ({repos.length})
            </h2>
            <div className="grid grid-cols-1 gap-4">
              {repos.map(repo => (
                <div
                  key={repo.id}
                  className="bg-gray-700 rounded-lg p-6 hover:bg-gray-600 transition-colors"
                >
                  <div className="flex items-start justify-between mb-3">
                    <div className="flex-1">
                      <a
                        href={repo.html_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-xl font-semibold text-blue-400 hover:text-blue-300 flex items-center"
                      >
                        {repo.full_name}
                        <ExternalLink className="w-4 h-4 ml-2" />
                      </a>
                      <p className="text-gray-300 mt-2">{repo.description}</p>
                    </div>
                  </div>

                  <div className="flex flex-wrap gap-4 mb-3 text-sm text-gray-400">
                    <div className="flex items-center">
                      <Star className="w-4 h-4 mr-1 text-yellow-400" />
                      {repo.stargazers_count.toLocaleString()}
                    </div>
                    <div className="flex items-center">
                      <GitFork className="w-4 h-4 mr-1" />
                      {repo.forks_count.toLocaleString()}
                    </div>
                    <div className="flex items-center">
                      <Eye className="w-4 h-4 mr-1" />
                      {repo.watchers_count.toLocaleString()}
                    </div>
                    {repo.language !== 'Unknown' && (
                      <span className="px-2 py-1 bg-blue-600 bg-opacity-30 rounded text-xs">
                        {repo.language}
                      </span>
                    )}
                    <div className="flex items-center">
                      <Calendar className="w-4 h-4 mr-1" />
                      Updated: {repo.updated_at}
                    </div>
                  </div>

                  {repo.topics.length > 0 && (
                    <div className="flex flex-wrap gap-2">
                      {repo.topics.map(topic => (
                        <span
                          key={topic}
                          className="px-2 py-1 bg-gray-600 rounded-full text-xs text-gray-300"
                        >
                          {topic}
                        </span>
                      ))}
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default GitHubStarsAnalyzer;