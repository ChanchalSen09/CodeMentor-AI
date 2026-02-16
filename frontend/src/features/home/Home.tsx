import { useEffect } from 'react'
import { useAuthStore } from '@/app/store/auth.store'
import { useProblemStore } from '@/app/store/problem.store'
import { useHealth } from '@/hooks/useHealth'

export default function Home() {
  const { isAuthenticated, user, fetchProfile } = useAuthStore()
  const { problems, fetchProblems } = useProblemStore()
  const { health, isLoading: healthLoading } = useHealth()

  useEffect(() => {
    if (isAuthenticated && !user) {
      fetchProfile()
    }
  }, [isAuthenticated, user, fetchProfile])

  useEffect(() => {
    if (isAuthenticated) {
      fetchProblems()
    }
  }, [isAuthenticated, fetchProblems])

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8">
        <header className="mb-12 text-center">
          <h1 className="text-5xl font-bold text-gray-900 mb-4">
            Welcome to <span className="text-primary-600">CodeMentor-AI</span>
          </h1>
          <p className="text-xl text-gray-700 max-w-2xl mx-auto">
            Your AI-powered companion for mastering Data Structures and Algorithms
          </p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
          <div className="bg-white rounded-lg shadow-md p-6">
            <h3 className="text-xl font-semibold mb-3 text-gray-800">System Status</h3>
            {healthLoading ? (
              <p className="text-gray-600">Checking system health...</p>
            ) : health ? (
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <span className="text-gray-600">API Status:</span>
                  <span
                    className={`font-semibold ${
                      health.status === 'healthy' ? 'text-green-600' : 'text-red-600'
                    }`}
                  >
                    {health.status}
                  </span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-gray-600">Database:</span>
                  <span
                    className={`font-semibold ${
                      health.database === 'connected' ? 'text-green-600' : 'text-red-600'
                    }`}
                  >
                    {health.database}
                  </span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-gray-600">Cache:</span>
                  <span
                    className={`font-semibold ${
                      health.cache === 'connected' ? 'text-green-600' : 'text-red-600'
                    }`}
                  >
                    {health.cache}
                  </span>
                </div>
              </div>
            ) : (
              <p className="text-red-600">Failed to fetch system health</p>
            )}
          </div>

          {isAuthenticated && user && (
            <div className="bg-white rounded-lg shadow-md p-6">
              <h3 className="text-xl font-semibold mb-3 text-gray-800">Your Profile</h3>
              <div className="space-y-2">
                <p className="text-gray-600">
                  <span className="font-medium">Username:</span> {user.username}
                </p>
                <p className="text-gray-600">
                  <span className="font-medium">Email:</span> {user.email}
                </p>
              </div>
            </div>
          )}

          <div className="bg-white rounded-lg shadow-md p-6">
            <h3 className="text-xl font-semibold mb-3 text-gray-800">Getting Started</h3>
            <ul className="space-y-2 text-gray-600">
              <li>• Browse coding problems</li>
              <li>• Get AI-powered hints</li>
              <li>• Submit your solutions</li>
              <li>• Track your progress</li>
            </ul>
          </div>
        </div>

        {isAuthenticated && problems.length > 0 && (
          <div className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-2xl font-bold mb-4 text-gray-800">Available Problems</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {problems.slice(0, 6).map((problem) => (
                <div key={problem.id} className="border border-gray-200 rounded-lg p-4">
                  <h3 className="font-semibold text-lg mb-2">{problem.title}</h3>
                  <div className="flex items-center gap-2 mb-2">
                    <span
                      className={`text-xs px-2 py-1 rounded ${
                        problem.difficulty === 'easy'
                          ? 'bg-green-100 text-green-800'
                          : problem.difficulty === 'medium'
                            ? 'bg-yellow-100 text-yellow-800'
                            : 'bg-red-100 text-red-800'
                      }`}
                    >
                      {problem.difficulty}
                    </span>
                  </div>
                  <div className="flex flex-wrap gap-1">
                    {problem.tags.slice(0, 3).map((tag, idx) => (
                      <span
                        key={idx}
                        className="text-xs bg-gray-100 text-gray-700 px-2 py-1 rounded"
                      >
                        {tag}
                      </span>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {!isAuthenticated && (
          <div className="bg-white rounded-lg shadow-md p-8 text-center">
            <h2 className="text-2xl font-bold mb-4 text-gray-800">Ready to Start?</h2>
            <p className="text-gray-600 mb-6">
              Sign up now to access hundreds of coding problems and AI-powered learning tools.
            </p>
            <div className="flex gap-4 justify-center">
              <a
                href="/login"
                className="px-6 py-3 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition"
              >
                Login
              </a>
              <a
                href="/register"
                className="px-6 py-3 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 transition"
              >
                Sign Up
              </a>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
