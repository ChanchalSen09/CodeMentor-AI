import { apiClient } from './api-client'
import { User, AuthTokens, LoginCredentials, RegisterData } from '@/types'

export const authService = {
  async login(credentials: LoginCredentials): Promise<AuthTokens> {
    const data = await apiClient.post<AuthTokens>('/auth/login/', credentials)
    localStorage.setItem('access_token', data.access)
    localStorage.setItem('refresh_token', data.refresh)
    return data
  },

  async register(data: RegisterData): Promise<{ user: User; tokens: AuthTokens }> {
    const response = await apiClient.post<{ user: User; tokens: AuthTokens }>(
      '/auth/register/',
      data
    )
    localStorage.setItem('access_token', response.tokens.access)
    localStorage.setItem('refresh_token', response.tokens.refresh)
    return response
  },

  logout(): void {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
  },

  async getProfile(): Promise<User> {
    return apiClient.get<User>('/auth/profile/')
  },

  async updateProfile(data: Partial<User>): Promise<User> {
    return apiClient.patch<User>('/auth/profile/update/', data)
  },

  isAuthenticated(): boolean {
    return !!localStorage.getItem('access_token')
  },
}
