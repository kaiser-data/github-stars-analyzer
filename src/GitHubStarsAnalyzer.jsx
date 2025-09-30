import React, { useState } from 'react';
import {
  Star,
  GitFork,
  Eye,
  Calendar,
  ExternalLink,
  Download,
  AlertCircle,
  Github,
  Trophy,
  Medal,
  Award,
  TrendingUp,
  Filter,
  X,
  Flame,
  Zap,
  Sparkles,
  Moon,
  ChevronDown,
  ChevronUp,
  Loader,
  BarChart3
} from 'lucide-react';

const GitHubStarsAnalyzer = () => {
  const [username, setUsername] = useState('');
  const [token, setToken] = useState('');
  const [repos, setRepos] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [summary, setSummary] = useState(null);

  // New state for sorting and filtering
  const [sortBy, setSortBy] = useState('stars');
  const [sortOrder, setSortOrder] = useState('desc');
  const [filterLanguage, setFilterLanguage] = useState('all');
  const [filterTopic, setFilterTopic] = useState('all');
  const [viewMode, setViewMode] = useState('all');

  // State for trend analysis
  const [repoTrends, setRepoTrends] = useState({});
  const [loadingTrends, setLoadingTrends] = useState(new Set());
  const [trendsFetched, setTrendsFetched] = useState(new Set());
  const [expandedTrends, setExpandedTrends] = useState(new Set());

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

  // Topic normalization helper
  const normalizeTopics = (topics) => {
    const topicMap = {};
    const normalizedTopics = new Set();

    // Common abbreviation mappings and normalizations
    const abbreviations = {
      'ai': 'artificial-intelligence',
      'ml': 'machine-learning',
      'dl': 'deep-learning',
      'nlp': 'natural-language-processing',
      'cv': 'computer-vision',
      'api': 'api',
      'rest': 'rest-api',
      'graphql': 'graphql',
      'db': 'database',
      'js': 'javascript',
      'ts': 'typescript',
      'py': 'python',
      'css': 'css',
      'html': 'html',
      'ui': 'user-interface',
      'ux': 'user-experience',
      'cli': 'command-line',
      'devops': 'devops',
      'cicd': 'ci-cd',
      'k8s': 'kubernetes',
      'aws': 'aws',
      'gcp': 'google-cloud',
      'iot': 'internet-of-things',
      'ci': 'continuous-integration',
      'cd': 'continuous-deployment'
    };

    // Pluralization rules
    const singularize = (word) => {
      if (word.endsWith('ies')) return word.slice(0, -3) + 'y';
      if (word.endsWith('es')) return word.slice(0, -2);
      if (word.endsWith('s') && !word.endsWith('ss')) return word.slice(0, -1);
      return word;
    };

    topics.forEach(topic => {
      let normalized = topic.toLowerCase().trim();

      // Check if it's a known abbreviation
      if (abbreviations[normalized]) {
        normalized = abbreviations[normalized];
      }

      // Try to match singular/plural variations
      const singular = singularize(normalized);

      // If we've seen the singular form, use that
      if (topicMap[singular]) {
        topicMap[singular].push(topic);
      } else if (topicMap[normalized]) {
        topicMap[normalized].push(topic);
      } else {
        // Check if a plural/singular version already exists
        let found = false;
        for (let existing in topicMap) {
          if (singularize(existing) === singular || existing === singular) {
            topicMap[existing].push(topic);
            found = true;
            break;
          }
        }
        if (!found) {
          topicMap[singular] = [topic];
        }
      }

      normalizedTopics.add(topicMap[singular] ? singular : normalized);
    });

    return { topicMap, normalizedTopics: Array.from(normalizedTopics) };
  };

  const generateSummary = (reposData) => {
    const totalRepos = reposData.length;
    const totalStars = reposData.reduce((sum, repo) => sum + repo.stargazers_count, 0);
    const avgStars = Math.round(totalStars / totalRepos);

    const languageCounts = {};
    const topicCounts = {};
    const topicVariations = {}; // Maps normalized topic -> array of original variations

    reposData.forEach(repo => {
      if (repo.language !== 'Unknown') {
        languageCounts[repo.language] = (languageCounts[repo.language] || 0) + 1;
      }

      // Normalize topics for counting
      const uniqueNormalized = new Set();
      repo.topics.forEach(topic => {
        let normalized = topic.toLowerCase().trim();

        // Apply abbreviation mapping FIRST
        const abbreviations = {
          'ai': 'artificial-intelligence',
          'ml': 'machine-learning',
          'dl': 'deep-learning',
          'nlp': 'natural-language-processing',
          'cv': 'computer-vision',
          'db': 'database',
          'js': 'javascript',
          'ts': 'typescript',
          'py': 'python',
          'ui': 'user-interface',
          'ux': 'user-experience',
          'cli': 'command-line',
          'cicd': 'ci-cd',
          'k8s': 'kubernetes',
          'iot': 'internet-of-things',
          'api': 'api',
          'rest-api': 'rest-api',
          'graphql': 'graphql'
        };

        // Check exact match first
        if (abbreviations[normalized]) {
          normalized = abbreviations[normalized];
        } else {
          // Singularize for grouping (improved rules)
          // Handle -ies -> -y (e.g., libraries -> library)
          if (normalized.endsWith('ies') && normalized.length > 4) {
            normalized = normalized.slice(0, -3) + 'y';
          }
          // Handle -es (but not -ess, -ness, -less)
          else if (normalized.endsWith('es') && !normalized.endsWith('ess') &&
                   !normalized.endsWith('ness') && !normalized.endsWith('less') &&
                   normalized.length > 3) {
            // Check if it's a real plural (e.g., "boxes" -> "box", but not "redis" stays "redis")
            const possibleSingular = normalized.slice(0, -2);
            // Only remove 'es' if the stem ends with s, x, z, ch, sh
            if (possibleSingular.endsWith('s') || possibleSingular.endsWith('x') ||
                possibleSingular.endsWith('z') || possibleSingular.endsWith('ch') ||
                possibleSingular.endsWith('sh')) {
              normalized = possibleSingular;
            }
          }
          // Handle regular plurals -s (but not -ss, -us, -as)
          else if (normalized.endsWith('s') && !normalized.endsWith('ss') &&
                   !normalized.endsWith('us') && !normalized.endsWith('as') &&
                   !normalized.endsWith('is') && normalized.length > 3) {
            // Don't singularize words that are commonly not plurals
            const nonPlurals = ['redis', 'postgres', 'canvas', 'cors', 'sass', 'less', 'css',
                               'express', 'cypress', 'aws', 'ios', 'macos', 'devops', 'kubernetes'];
            if (!nonPlurals.includes(normalized)) {
              normalized = normalized.slice(0, -1);
            }
          }
        }

        uniqueNormalized.add(normalized);

        // Track variations
        if (!topicVariations[normalized]) {
          topicVariations[normalized] = new Set();
        }
        topicVariations[normalized].add(topic);
      });

      // Count each normalized topic once per repo
      uniqueNormalized.forEach(normalized => {
        topicCounts[normalized] = (topicCounts[normalized] || 0) + 1;
      });
    });

    const topLanguages = Object.entries(languageCounts)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5)
      .map(([lang, count]) => ({ language: lang, count }));

    const topTopics = Object.entries(topicCounts)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10)
      .map(([topic, count]) => ({
        topic,
        count,
        variations: Array.from(topicVariations[topic] || [topic])
      }));

    const mostStarred = [...reposData]
      .sort((a, b) => b.stargazers_count - a.stargazers_count)
      .slice(0, 5);

    // Get all unique languages and topics for filter dropdowns
    const allLanguages = Object.keys(languageCounts).sort();

    // Get top 20 topics only for the filter dropdown with their variations
    const topTopicsForFilter = Object.entries(topicCounts)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 20)
      .map(([topic]) => ({
        normalized: topic,
        display: topic,
        variations: Array.from(topicVariations[topic] || [topic]),
        count: topicCounts[topic]
      }));

    // Debug logging
    console.log('Topic Normalization Debug:');
    console.log('Total unique normalized topics:', Object.keys(topicCounts).length);
    console.log('Top 20 topics with variations:', topTopicsForFilter.map(t =>
      `${t.display} (${t.count}) - variations: [${t.variations.join(', ')}]`
    ));

    setSummary({
      totalRepos,
      totalStars,
      avgStars,
      topLanguages,
      topTopics,
      mostStarred,
      allLanguages,
      allTopics: topTopicsForFilter,
      topicVariations // Store for filtering
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

  // Sorting and filtering function
  const getSortedAndFilteredRepos = () => {
    let filtered = [...repos];

    // Apply view mode filters
    if (viewMode === 'top-starred') {
      filtered = filtered.sort((a, b) => b.stargazers_count - a.stargazers_count).slice(0, 20);
    } else if (viewMode === 'top-forked') {
      filtered = filtered.sort((a, b) => b.forks_count - a.forks_count).slice(0, 20);
    } else if (viewMode === 'top-watchers') {
      filtered = filtered.sort((a, b) => b.watchers_count - a.watchers_count).slice(0, 20);
    } else if (viewMode === 'recent') {
      filtered = filtered.sort((a, b) => new Date(b.updated_at) - new Date(a.updated_at)).slice(0, 20);
    }

    // Apply language filter
    if (filterLanguage !== 'all') {
      filtered = filtered.filter(r => r.language === filterLanguage);
    }

    // Apply topic filter with normalization
    if (filterTopic !== 'all') {
      if (filterTopic === 'others') {
        // Filter for repos with topics not in the top 20
        const topNormalizedTopics = (summary?.allTopics || []).map(t => t.normalized);
        filtered = filtered.filter(r => {
          if (r.topics.length === 0) return false;

          // Check if any of the repo's topics normalize to a top 20 topic
          return !r.topics.some(topic => {
            let normalized = topic.toLowerCase().trim();

            // Apply same normalization as in generateSummary
            const abbreviations = {
              'ai': 'artificial-intelligence',
              'ml': 'machine-learning',
              'dl': 'deep-learning',
              'nlp': 'natural-language-processing',
              'cv': 'computer-vision',
              'db': 'database',
              'js': 'javascript',
              'ts': 'typescript',
              'py': 'python',
              'ui': 'user-interface',
              'ux': 'user-experience',
              'cli': 'command-line',
              'cicd': 'ci-cd',
              'k8s': 'kubernetes',
              'iot': 'internet-of-things',
              'api': 'api',
              'rest-api': 'rest-api',
              'graphql': 'graphql'
            };

            if (abbreviations[normalized]) {
              normalized = abbreviations[normalized];
            } else {
              // Improved singularization
              if (normalized.endsWith('ies') && normalized.length > 4) {
                normalized = normalized.slice(0, -3) + 'y';
              } else if (normalized.endsWith('es') && !normalized.endsWith('ess') &&
                         !normalized.endsWith('ness') && !normalized.endsWith('less') &&
                         normalized.length > 3) {
                const possibleSingular = normalized.slice(0, -2);
                if (possibleSingular.endsWith('s') || possibleSingular.endsWith('x') ||
                    possibleSingular.endsWith('z') || possibleSingular.endsWith('ch') ||
                    possibleSingular.endsWith('sh')) {
                  normalized = possibleSingular;
                }
              } else if (normalized.endsWith('s') && !normalized.endsWith('ss') &&
                         !normalized.endsWith('us') && !normalized.endsWith('as') &&
                         !normalized.endsWith('is') && normalized.length > 3) {
                const nonPlurals = ['redis', 'postgres', 'canvas', 'cors', 'sass', 'less', 'css',
                                   'express', 'cypress', 'aws', 'ios', 'macos', 'devops', 'kubernetes'];
                if (!nonPlurals.includes(normalized)) {
                  normalized = normalized.slice(0, -1);
                }
              }
            }

            return topNormalizedTopics.includes(normalized);
          });
        });
      } else {
        // Filter for repos that have any variation of the selected topic
        const selectedTopicData = (summary?.allTopics || []).find(t => t.normalized === filterTopic);
        const variations = selectedTopicData?.variations || [filterTopic];

        filtered = filtered.filter(r =>
          r.topics.some(topic => variations.includes(topic))
        );
      }
    }

    // Apply sorting (only if in 'all' view mode)
    if (viewMode === 'all') {
      filtered.sort((a, b) => {
        let aVal, bVal;
        switch (sortBy) {
          case 'stars':
            aVal = a.stargazers_count;
            bVal = b.stargazers_count;
            break;
          case 'forks':
            aVal = a.forks_count;
            bVal = b.forks_count;
            break;
          case 'watchers':
            aVal = a.watchers_count;
            bVal = b.watchers_count;
            break;
          case 'updated':
            aVal = new Date(a.updated_at);
            bVal = new Date(b.updated_at);
            break;
          case 'name':
            aVal = a.name.toLowerCase();
            bVal = b.name.toLowerCase();
            break;
          case 'issues':
            aVal = a.open_issues_count;
            bVal = b.open_issues_count;
            break;
          case 'last30days':
            aVal = repoTrends[a.id]?.last30Days?.count || 0;
            bVal = repoTrends[b.id]?.last30Days?.count || 0;
            break;
          case 'last90days':
            aVal = repoTrends[a.id]?.last90Days?.count || 0;
            bVal = repoTrends[b.id]?.last90Days?.count || 0;
            break;
          case 'momentum':
            aVal = repoTrends[a.id]?.momentumPercent || 0;
            bVal = repoTrends[b.id]?.momentumPercent || 0;
            break;
          default:
            aVal = a.stargazers_count;
            bVal = b.stargazers_count;
        }

        if (typeof aVal === 'string') {
          return sortOrder === 'desc' ? bVal.localeCompare(aVal) : aVal.localeCompare(bVal);
        }
        return sortOrder === 'desc' ? bVal - aVal : aVal - bVal;
      });
    }

    return filtered;
  };

  // Get ranking badge
  const getRankBadge = (index) => {
    if (index === 0) return { icon: '🥇', color: 'text-yellow-400', label: '#1', name: 'Gold' };
    if (index === 1) return { icon: '🥈', color: 'text-gray-300', label: '#2', name: 'Silver' };
    if (index === 2) return { icon: '🥉', color: 'text-orange-400', label: '#3', name: 'Bronze' };
    return { icon: '', color: 'text-gray-400', label: `#${index + 1}`, name: '' };
  };

  // Reset filters
  const resetFilters = () => {
    setSortBy('stars');
    setSortOrder('desc');
    setFilterLanguage('all');
    setFilterTopic('all');
    setViewMode('all');
  };

  // Fetch star history for a repository
  const fetchStarHistory = async (owner, repoName, repoId) => {
    // Check if already loading or fetched
    if (loadingTrends.has(repoId) || trendsFetched.has(repoId)) {
      return;
    }

    setLoadingTrends(prev => new Set([...prev, repoId]));

    try {
      const headers = {
        'Accept': 'application/vnd.github.star+json'
      };

      if (token.trim()) {
        headers['Authorization'] = `token ${token}`;
      }

      console.log(`Fetching star history for ${owner}/${repoName}...`);

      const response = await fetch(
        `https://api.github.com/repos/${owner}/${repoName}/stargazers?per_page=100`,
        { headers }
      );

      if (!response.ok) {
        const errorText = await response.text();
        console.error(`API Error ${response.status}:`, errorText);
        throw new Error(`Failed to fetch star history: ${response.status}`);
      }

      const stargazers = await response.json();
      console.log(`Received ${stargazers.length} stargazers for ${owner}/${repoName}`);

      // Log first few starred_at dates for debugging
      if (stargazers.length > 0) {
        console.log('Sample starred_at dates:', stargazers.slice(0, 3).map(s => s.starred_at));
      }

      const trends = calculateTrends(stargazers);
      console.log(`Calculated trends for ${owner}/${repoName}:`, trends);

      setRepoTrends(prev => ({
        ...prev,
        [repoId]: {
          ...trends,
          fetchedAt: new Date().toISOString()
        }
      }));

      setTrendsFetched(prev => new Set([...prev, repoId]));
    } catch (err) {
      console.error(`Error fetching trends for ${owner}/${repoName}:`, err);
      setError(`Failed to fetch trends for ${owner}/${repoName}: ${err.message}`);
    } finally {
      setLoadingTrends(prev => {
        const newSet = new Set(prev);
        newSet.delete(repoId);
        return newSet;
      });
    }
  };

  // Calculate trends from stargazer data
  const calculateTrends = (stargazers) => {
    const now = new Date();
    const periods = {
      last30Days: 30,
      last90Days: 90,
      last180Days: 180,
      last365Days: 365
    };

    const trends = {};

    console.log('Calculating trends...');
    console.log('Current date:', now.toISOString());
    console.log('Total stargazers received:', stargazers.length);

    Object.entries(periods).forEach(([key, days]) => {
      const cutoff = new Date(now.getTime() - days * 24 * 60 * 60 * 1000);
      console.log(`${key} cutoff date:`, cutoff.toISOString());

      const count = stargazers.filter(s => {
        const starDate = new Date(s.starred_at);
        return starDate > cutoff;
      }).length;

      const rate = Math.round((count / days) * 30); // Monthly rate
      console.log(`${key}: ${count} stars, ${rate}/month`);

      trends[key] = { count, rate };
    });

    // Calculate trend classification based on 30-day stars
    const monthlyStars = trends.last30Days.count;
    let trendEmoji = '💤';
    let trendLabel = 'Quiet';

    if (monthlyStars > 100) {
      trendEmoji = '🔥';
      trendLabel = 'Hot';
    } else if (monthlyStars >= 10) {
      trendEmoji = '⚡';
      trendLabel = 'Rising';
    } else if (monthlyStars >= 1) {
      trendEmoji = '✨';
      trendLabel = 'Steady';
    }

    trends.trend = `${trendEmoji} ${trendLabel}`;

    // Calculate momentum
    const rate30 = trends.last30Days.rate;
    const rate90 = trends.last90Days.rate;
    const diff = ((rate30 - rate90) / (rate90 || 1)) * 100;

    let momentum = '➡️ Stable';
    if (diff > 20) {
      momentum = '📈 Accelerating';
    } else if (diff < -20) {
      momentum = '📉 Slowing';
    }

    trends.momentum = momentum;
    trends.momentumPercent = Math.round(diff);

    console.log('Final trends:', trends);
    return trends;
  };

  // Fetch trends for top repos
  const fetchTopTrends = async () => {
    const topRepos = getSortedAndFilteredRepos().slice(0, 20);

    for (const repo of topRepos) {
      if (!trendsFetched.has(repo.id)) {
        await fetchStarHistory(repo.owner, repo.name, repo.id);
        // Small delay to avoid rate limiting
        await new Promise(resolve => setTimeout(resolve, 100));
      }
    }
  };

  // Toggle trend expansion
  const toggleTrendExpansion = (repoId) => {
    setExpandedTrends(prev => {
      const newSet = new Set(prev);
      if (newSet.has(repoId)) {
        newSet.delete(repoId);
      } else {
        newSet.add(repoId);
      }
      return newSet;
    });
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
                <h3 className="text-xl font-bold mb-4">Popular Topics (Normalized)</h3>
                {summary.topTopics.length > 0 ? (
                  <div className="flex flex-wrap gap-2">
                    {summary.topTopics.map(topicData => (
                      <span
                        key={topicData.topic}
                        className="px-3 py-1 bg-blue-600 bg-opacity-30 border border-blue-500 rounded-full text-sm"
                        title={`Variations: ${topicData.variations.join(', ')}`}
                      >
                        {topicData.topic} ({topicData.count})
                        {topicData.variations.length > 1 && (
                          <span className="text-xs text-blue-300"> [{topicData.variations.length}]</span>
                        )}
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
            <h2 className="text-2xl font-bold mb-6 flex items-center">
              <Trophy className="w-6 h-6 mr-2 text-yellow-400" />
              Repository Rankings
            </h2>

            {/* Fetch Trends Button */}
            <div className="bg-blue-900 bg-opacity-30 border border-blue-500 rounded-lg p-4 mb-6">
              <div className="flex items-center justify-between flex-wrap gap-4">
                <div className="flex items-center">
                  <BarChart3 className="w-5 h-5 mr-3 text-blue-400" />
                  <div>
                    <p className="text-white font-medium">Recent Trend Analysis</p>
                    <p className="text-sm text-gray-300">
                      Fetch star history for the last 30/90/180/365 days
                    </p>
                  </div>
                </div>
                <button
                  onClick={fetchTopTrends}
                  disabled={loadingTrends.size > 0}
                  className="flex items-center px-4 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 disabled:cursor-not-allowed rounded-lg font-medium transition-colors"
                >
                  {loadingTrends.size > 0 ? (
                    <>
                      <Loader className="w-4 h-4 mr-2 animate-spin" />
                      Loading {loadingTrends.size} repos...
                    </>
                  ) : (
                    <>
                      <TrendingUp className="w-4 h-4 mr-2" />
                      Load Top 20 Trends
                    </>
                  )}
                </button>
              </div>
            </div>

            {/* View Mode Tabs */}
            <div className="bg-gray-800 rounded-lg p-4 mb-6">
              <div className="flex flex-wrap gap-2">
                <button
                  onClick={() => setViewMode('all')}
                  className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                    viewMode === 'all'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
                  }`}
                >
                  All Repos
                </button>
                <button
                  onClick={() => setViewMode('top-starred')}
                  className={`px-4 py-2 rounded-lg font-medium transition-colors flex items-center ${
                    viewMode === 'top-starred'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
                  }`}
                >
                  <Star className="w-4 h-4 mr-1" />
                  Most Starred
                </button>
                <button
                  onClick={() => setViewMode('top-forked')}
                  className={`px-4 py-2 rounded-lg font-medium transition-colors flex items-center ${
                    viewMode === 'top-forked'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
                  }`}
                >
                  <GitFork className="w-4 h-4 mr-1" />
                  Most Forked
                </button>
                <button
                  onClick={() => setViewMode('top-watchers')}
                  className={`px-4 py-2 rounded-lg font-medium transition-colors flex items-center ${
                    viewMode === 'top-watchers'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
                  }`}
                >
                  <Eye className="w-4 h-4 mr-1" />
                  Most Active
                </button>
                <button
                  onClick={() => setViewMode('recent')}
                  className={`px-4 py-2 rounded-lg font-medium transition-colors flex items-center ${
                    viewMode === 'recent'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
                  }`}
                >
                  <TrendingUp className="w-4 h-4 mr-1" />
                  Recently Updated
                </button>
              </div>
            </div>

            {/* Sort & Filter Controls */}
            <div className="bg-gray-800 rounded-lg shadow-2xl p-6 mb-6">
              <div className="flex items-center mb-4">
                <Filter className="w-5 h-5 mr-2 text-blue-400" />
                <h3 className="text-xl font-bold text-white">Sort & Filter</h3>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                {/* Sort By */}
                {viewMode === 'all' && (
                  <>
                    <div>
                      <label className="block text-sm text-gray-400 mb-2">Sort By</label>
                      <select
                        value={sortBy}
                        onChange={(e) => setSortBy(e.target.value)}
                        className="w-full px-3 py-2 bg-gray-700 text-white rounded-lg border border-gray-600 focus:outline-none focus:border-blue-500"
                      >
                        <option value="stars">Stars</option>
                        <option value="forks">Forks</option>
                        <option value="watchers">Watchers</option>
                        <option value="updated">Recently Updated</option>
                        <option value="name">Name</option>
                        <option value="issues">Open Issues</option>
                        <option value="last30days">Last 30 Days ⚡</option>
                        <option value="last90days">Last 3 Months</option>
                        <option value="momentum">Momentum 📈</option>
                      </select>
                    </div>

                    {/* Sort Order */}
                    <div>
                      <label className="block text-sm text-gray-400 mb-2">Order</label>
                      <select
                        value={sortOrder}
                        onChange={(e) => setSortOrder(e.target.value)}
                        className="w-full px-3 py-2 bg-gray-700 text-white rounded-lg border border-gray-600 focus:outline-none focus:border-blue-500"
                      >
                        <option value="desc">Descending</option>
                        <option value="asc">Ascending</option>
                      </select>
                    </div>
                  </>
                )}

                {/* Filter Language */}
                <div>
                  <label className="block text-sm text-gray-400 mb-2">Language</label>
                  <select
                    value={filterLanguage}
                    onChange={(e) => setFilterLanguage(e.target.value)}
                    className="w-full px-3 py-2 bg-gray-700 text-white rounded-lg border border-gray-600 focus:outline-none focus:border-blue-500"
                  >
                    <option value="all">All Languages</option>
                    {summary?.allLanguages.map((lang) => (
                      <option key={lang} value={lang}>
                        {lang}
                      </option>
                    ))}
                  </select>
                </div>

                {/* Filter Topic */}
                <div>
                  <label className="block text-sm text-gray-400 mb-2">
                    Topic (Top 20, normalized)
                  </label>
                  <select
                    value={filterTopic}
                    onChange={(e) => setFilterTopic(e.target.value)}
                    className="w-full px-3 py-2 bg-gray-700 text-white rounded-lg border border-gray-600 focus:outline-none focus:border-blue-500"
                  >
                    <option value="all">All Topics</option>
                    {summary?.allTopics.map((topicData) => (
                      <option key={topicData.normalized} value={topicData.normalized}>
                        {topicData.display} ({topicData.count})
                        {topicData.variations.length > 1 && ` [${topicData.variations.length} variants]`}
                      </option>
                    ))}
                    <option value="others">Others (not in top 20)</option>
                  </select>
                </div>
              </div>

              {/* Active Filters Display */}
              {(filterLanguage !== 'all' || filterTopic !== 'all') && (
                <div className="mt-4 flex flex-wrap items-center gap-2">
                  <span className="text-gray-400 text-sm">Active filters:</span>
                  {filterLanguage !== 'all' && (
                    <span className="bg-blue-900/50 text-blue-200 px-3 py-1 rounded-full text-sm flex items-center gap-2">
                      {filterLanguage}
                      <button
                        onClick={() => setFilterLanguage('all')}
                        className="hover:text-white"
                      >
                        <X className="w-3 h-3" />
                      </button>
                    </span>
                  )}
                  {filterTopic !== 'all' && (
                    <span className="bg-blue-900/50 text-blue-200 px-3 py-1 rounded-full text-sm flex items-center gap-2">
                      {filterTopic}
                      <button onClick={() => setFilterTopic('all')} className="hover:text-white">
                        <X className="w-3 h-3" />
                      </button>
                    </span>
                  )}
                  <button
                    onClick={resetFilters}
                    className="text-red-400 text-sm hover:text-red-300 underline"
                  >
                    Reset All
                  </button>
                </div>
              )}

              {/* Results Counter */}
              <div className="mt-4 text-gray-400 text-sm">
                Showing <span className="text-white font-semibold">{getSortedAndFilteredRepos().length}</span> of{' '}
                <span className="text-white font-semibold">{repos.length}</span> repositories
              </div>
            </div>

            {/* Repository Cards with Rankings */}
            <div className="grid grid-cols-1 gap-4">
              {getSortedAndFilteredRepos().map((repo, index) => {
                const rankBadge = getRankBadge(index);
                return (
                <div
                  key={repo.id}
                  className={`bg-gray-700 rounded-lg p-6 hover:bg-gray-600 transition-all ${
                    index < 3 ? 'border-2 border-yellow-500/30' : ''
                  }`}
                >
                  {/* Ranking Badge */}
                  <div className="flex items-center justify-between mb-3">
                    <div className="flex items-center gap-3">
                      <span className={`text-3xl font-bold ${rankBadge.color}`}>
                        {rankBadge.icon} {rankBadge.label}
                      </span>
                      {index < 3 && (
                        <span className="bg-yellow-900/30 text-yellow-300 px-3 py-1 rounded-full text-xs font-semibold flex items-center gap-1">
                          <Award className="w-3 h-3" />
                          Top {index + 1}
                        </span>
                      )}
                    </div>
                  </div>

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
                    <div className="flex flex-wrap gap-2 mb-3">
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

                  {/* Trends Section */}
                  <div className="mt-4 pt-4 border-t border-gray-600">
                    {!trendsFetched.has(repo.id) && !loadingTrends.has(repo.id) && (
                      <button
                        onClick={() => fetchStarHistory(repo.owner, repo.name, repo.id)}
                        className="flex items-center px-3 py-2 bg-blue-600 hover:bg-blue-700 rounded-lg text-sm font-medium transition-colors"
                      >
                        <TrendingUp className="w-4 h-4 mr-2" />
                        Show Recent Trends
                      </button>
                    )}

                    {loadingTrends.has(repo.id) && (
                      <div className="flex items-center text-blue-400 text-sm">
                        <Loader className="w-4 h-4 mr-2 animate-spin" />
                        Loading trend data...
                      </div>
                    )}

                    {trendsFetched.has(repo.id) && repoTrends[repo.id] && (
                      <div className="space-y-3">
                        <div className="flex items-center justify-between">
                          <button
                            onClick={() => toggleTrendExpansion(repo.id)}
                            className="flex items-center text-white hover:text-blue-400 transition-colors"
                          >
                            <TrendingUp className="w-4 h-4 mr-2" />
                            <span className="font-semibold">Recent Activity</span>
                            {expandedTrends.has(repo.id) ? (
                              <ChevronUp className="w-4 h-4 ml-2" />
                            ) : (
                              <ChevronDown className="w-4 h-4 ml-2" />
                            )}
                          </button>
                          <div className="flex items-center gap-3">
                            <span className="text-lg">{repoTrends[repo.id].trend}</span>
                            <span className="text-sm text-gray-400">|</span>
                            <span className="text-lg">{repoTrends[repo.id].momentum}</span>
                          </div>
                        </div>

                        {expandedTrends.has(repo.id) && (
                          <div className="bg-gray-800 rounded-lg p-4 space-y-2">
                            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                              <div>
                                <p className="text-gray-400">Last 30 days</p>
                                <p className="text-white font-semibold">
                                  +{repoTrends[repo.id].last30Days.count} stars
                                </p>
                                <p className="text-xs text-gray-500">
                                  (~{repoTrends[repo.id].last30Days.rate}/month)
                                </p>
                              </div>
                              <div>
                                <p className="text-gray-400">Last 3 months</p>
                                <p className="text-white font-semibold">
                                  +{repoTrends[repo.id].last90Days.count} stars
                                </p>
                                <p className="text-xs text-gray-500">
                                  (~{repoTrends[repo.id].last90Days.rate}/month)
                                </p>
                              </div>
                              <div>
                                <p className="text-gray-400">Last 6 months</p>
                                <p className="text-white font-semibold">
                                  +{repoTrends[repo.id].last180Days.count} stars
                                </p>
                                <p className="text-xs text-gray-500">
                                  (~{repoTrends[repo.id].last180Days.rate}/month)
                                </p>
                              </div>
                              <div>
                                <p className="text-gray-400">Last year</p>
                                <p className="text-white font-semibold">
                                  +{repoTrends[repo.id].last365Days.count} stars
                                </p>
                                <p className="text-xs text-gray-500">
                                  (~{repoTrends[repo.id].last365Days.rate}/month)
                                </p>
                              </div>
                            </div>
                            <a
                              href={`https://star-history.com/#${repo.full_name}`}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="flex items-center text-blue-400 hover:text-blue-300 text-sm mt-3"
                            >
                              <BarChart3 className="w-4 h-4 mr-2" />
                              View Detailed History →
                            </a>
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                </div>
                );
              })}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default GitHubStarsAnalyzer;