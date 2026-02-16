import { apiClient } from './api-client'

interface HealthStatus {
  status: string
  database: string
  cache: string
}

export const healthService = {
  async checkHealth(): Promise<HealthStatus> {
    return apiClient.get<HealthStatus>('/health/')
  },
}
