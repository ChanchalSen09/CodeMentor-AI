import { create } from 'zustand'
import { User } from '@/types'
import { authService } from '@/services/auth.service'

interface AuthState {
  user: User | null
  isAuthenticated: boolean
  isLoading: boolean
  error: string | null
  login: (username: string, password: string) => Promise<void>
  register: (data: {
    username: string
    email: string
    password: string
    password_confirm: string
  }) => Promise<void>
  logout: () => void
  fetchProfile: () => Promise<void>
  clearError: () => void
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  isAuthenticated: authService.isAuthenticated(),
  isLoading: false,
  error: null,

  login: async (username, password) => {
    set({ isLoading: true, error: null })
    try {
      await authService.login({ username, password })
      const user = await authService.getProfile()
      set({ user, isAuthenticated: true, isLoading: false })
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Login failed'
      set({ error: message, isLoading: false })
      throw error
    }
  },

  register: async (data) => {
    set({ isLoading: true, error: null })
    try {
      const response = await authService.register(data)
      set({ user: response.user, isAuthenticated: true, isLoading: false })
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Registration failed'
      set({ error: message, isLoading: false })
      throw error
    }
  },

  logout: () => {
    authService.logout()
    set({ user: null, isAuthenticated: false })
  },

  fetchProfile: async () => {
    set({ isLoading: true, error: null })
    try {
      const user = await authService.getProfile()
      set({ user, isAuthenticated: true, isLoading: false })
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Failed to fetch profile'
      set({ error: message, isLoading: false, isAuthenticated: false })
    }
  },

  clearError: () => set({ error: null }),
}))
