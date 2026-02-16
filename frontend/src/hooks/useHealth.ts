import { useState, useEffect } from 'react'
import { healthService } from '@/services/health.service'

interface HealthStatus {
  status: string
  database: string
  cache: string
}

export const useHealth = () => {
  const [health, setHealth] = useState<HealthStatus | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const checkHealth = async () => {
      try {
        const status = await healthService.checkHealth()
        setHealth(status)
        setError(null)
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to check health')
      } finally {
        setIsLoading(false)
      }
    }

    checkHealth()
  }, [])

  return { health, isLoading, error }
}
