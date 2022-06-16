import * as React from 'react';
import { useState } from 'react';
import { Text, View, Button, StyleSheet } from 'react-native';

import { NavigationContainer } from '@react-navigation/native';
import { createMaterialBottomTabNavigator } from '@react-navigation/material-bottom-tabs';
import { MaterialCommunityIcons } from '@expo/vector-icons';

function Feed() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Feed!</Text>
    </View>
  );
}

function Profile() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Profile!</Text>
    </View>
  );
}

const toPaddedHex = (x: number) => x.toString(16).padStart(2, '0').toUpperCase()

const getRandomColorHex = () => {
  const red = toPaddedHex(Math.round(Math.random() * 255));
  const green = toPaddedHex(Math.round(Math.random() * 255));
  const blue = toPaddedHex(Math.round(Math.random() * 255));
  return "#" + red + green + blue;
}

import MapboxGL from "@react-native-mapbox-gl/maps";

MapboxGL.setAccessToken("pk.eyJ1IjoicGF1bHBoYW0iLCJhIjoiY2wxYTE4Nm83MDJ4MDNibzVvcGVrenJ0ZiJ9.QeVxgVkt8SWMfpM8JC8Xvg");

const mapStyles = StyleSheet.create({
  page: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#F5FCFF"
  },
  container: {
    height: 300,
    width: 300,
    backgroundColor: "tomato"
  },
  map: {
    flex: 1
  }
});

function MapScreen() {
  return (
    <View style={mapStyles.page}>
      <View style={mapStyles.container}>
        <MapboxGL.MapView style={mapStyles.map} />
      </View>
    </View>
  );
}

type SettingsScreenProps = {
  setGlobalColor: Function
}

function SettingsScreen(props: SettingsScreenProps) {
  const initialColor = getRandomColorHex();
  console.log(initialColor);
  return (
    <View style={{
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center'
      }}>
      <Button
        color={initialColor}
        onPress={() => {
          const randomColor = getRandomColorHex();
          props.setGlobalColor(randomColor);
        }}
        title="Randomize Text Color"
      ></Button>
      <Text>Settings!</Text>
    </View>
  );
}

const Tab = createMaterialBottomTabNavigator();

function MyTabs() {
  const [globalColor, setGlobalColor] = useState("#e91e63");

  return (
    <Tab.Navigator
      initialRouteName="Feed"
      activeColor={globalColor}
      labelStyle={{ fontSize: 12 }}
      style={{ backgroundColor: 'tomato' }}
    >
      <Tab.Screen
        name="Feed"
        component={Feed}
        options={{
          tabBarLabel: 'Home',
          tabBarIcon: ({ color }) => (
            <MaterialCommunityIcons name="home" color={color} size={26} />
          ),
        }}
      />
      <Tab.Screen
        name="Maps"
        component={MapScreen}
        options={{
          tabBarLabel: 'Maps',
          tabBarIcon: ({ color }) => (
            <MaterialCommunityIcons name="map-marker" color={color} size={26} />
          ),
        }}
      />
      <Tab.Screen
        name="Settings"
        component={() => <SettingsScreen setGlobalColor={setGlobalColor} />}
        options={{
          tabBarLabel: 'Settings',
          tabBarIcon: ({ color }) => (
            <MaterialCommunityIcons name="cog-outline" color={color} size={26} />
          ),
        }}
      />
      <Tab.Screen
        name="Profile"
        component={Profile}
        options={{
          tabBarLabel: 'Profile',
          tabBarIcon: ({ color }) => (
            <MaterialCommunityIcons name="account" color={color} size={26} />
          ),
        }}
      />
    </Tab.Navigator>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <MyTabs />
    </NavigationContainer>
  );
}