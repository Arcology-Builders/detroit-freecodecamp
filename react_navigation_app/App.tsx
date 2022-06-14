import * as React from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

//import { createStackNavigator } from '@react-navigation/stack';

const RootStack = createNativeStackNavigator<RootStackParamList>();

type RootStackParamList = {
  Home: undefined;
  Settings: undefined;
};

function HomeScreen() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Home!</Text>
    </View>
  );
}

function MapScreen() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Map!</Text>
    </View>
  );
}

function SettingsScreen(changeGlobalColor: Function) {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Button
        onPress={() => {
          const red = Math.round(Math.random() * 255).toString(16).toUpperCase;
          const green = Math.round(Math.random() * 255).toString(16).toUpperCase;
          const blue = Math.round(Math.random() * 255).toString(16).toUpperCase;
          const hexColorCode = "#" + red + green + blue;
          changeGlobalColor(hexColorCode);
        }}
        title="Randomize Text Color"
      ></Button>
      <Text>Settings!</Text>
    </View>
  );
}

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <View>
      <View style={styles.container}>
        <Text style={styles.bigBlue}>Hello Damien and Paul!</Text>
        <StatusBar style="auto" />
      </View>
      <NavigationContainer>
        <Tab.Navigator>
          <Tab.Screen name="Home Name" component={HomeScreen} />
          <Tab.Screen name="Maps Name" component={MapScreen} />          
          <Tab.Screen name="Settings Name" component={SettingsScreen} />
        </Tab.Navigator>
      </NavigationContainer>
    </View>
  );
}

const styles = StyleSheet.create({
  bigBlue: {
    color: 'blue',
    fontWeight: 'bold',
    fontSize: 130,
  },
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
