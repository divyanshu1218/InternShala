import React, * as ReactModule from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { ActivityIndicator, View } from 'react-native';
import * as SecureStore from 'expo-secure-store';

import LoginScreen from './src/screens/LoginScreen';
import SignupScreen from './src/screens/SignupScreen';
// Placeholders for now
import DashboardScreen from './src/screens/DashboardScreen';
import VideoPlayerScreen from './src/screens/VideoPlayerScreen';
import SettingsScreen from './src/screens/SettingsScreen';
import { authService } from './src/services/authService';

const Stack = createStackNavigator();
const Tab = createBottomTabNavigator();

// Auth Stack
function AuthStack({ setPayload }) {
  return (
    <Stack.Navigator screenOptions={{ headerShown: false }}>
      <Stack.Screen name="Login">
        {props => <LoginScreen {...props} setPayload={setPayload} />}
      </Stack.Screen>
      <Stack.Screen name="Signup" component={SignupScreen} />
    </Stack.Navigator>
  );
}

// App Stack (Authenticated)
function AppStack({ setPayload }) {
  // We need a nested stack for Dashboard -> VideoPlayer
  // But Tab navigator is usually the root of authenticated area
  return (
    <Stack.Navigator screenOptions={{ headerShown: false }}>
      <Stack.Screen name="MainTabs">
        {props => <MainTabNavigator {...props} setPayload={setPayload} />}
      </Stack.Screen>
      <Stack.Screen name="VideoPlayer" component={VideoPlayerScreen} />
    </Stack.Navigator>
  );
}

function MainTabNavigator({ setPayload }) {
  return (
    <Tab.Navigator>
      <Tab.Screen name="Dashboard" component={DashboardScreen} />
      <Tab.Screen name="Settings">
        {props => <SettingsScreen {...props} setPayload={setPayload} />}
      </Tab.Screen>
    </Tab.Navigator>
  );
}

export default function App() {
  const [isLoading, setIsLoading] = ReactModule.useState(true);
  const [isAuthenticated, setIsAuthenticated] = ReactModule.useState(false);

  ReactModule.useEffect(() => {
    checkAuth();
  }, [isAuthenticated]); // re-check if state flips

  const checkAuth = async () => {
    try {
      const token = await authService.getToken();
      setIsAuthenticated(!!token);
    } catch (e) {
      console.log('Auth check error', e);
    } finally {
      setIsLoading(false);
    }
  };

  if (isLoading) {
    return (
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        <ActivityIndicator size="large" />
      </View>
    );
  }

  return (
    <NavigationContainer>
      {isAuthenticated ? (
        <AppStack setPayload={setIsAuthenticated} />
      ) : (
        <AuthStack setPayload={setIsAuthenticated} />
      )}
    </NavigationContainer>
  );
}
