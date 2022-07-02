/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

const ACCESS_TOKEN = 'pk.eyJ1IjoiaGFubmFob3R0ZXIiLCJhIjoiY2t1b29sNzlnNGRkMDJwcTY4anlndXVubCJ9.SixIwkOZsOO2CuurXnRuKw';

const randomLongitude = Math.round(Math.random() * 180 * 2, 4) - 180;
const randomLatitude = Math.round(Math.random() * 85.0511 * 2, 4) - 85.0511;

// Lat/long for Bead Museum, to 4 places
const lon =-831088;
const lat =423562;

const fileReaderInstance = new FileReader();

import React, { useState, useEffect } from 'react';
import type {Node} from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  useColorScheme,
  View,
  Image,
  FlatList,
} from 'react-native';

import {
  Colors,
  DebugInstructions,
  Header,
  LearnMoreLinks,
  ReloadInstructions,
} from 'react-native/Libraries/NewAppScreen';

const Section = ({children, title}): Node => {
  const isDarkMode = useColorScheme() === 'dark';
  return (
    <View style={styles.sectionContainer}>
      <Text
        style={[
          styles.sectionTitle,
          {
            color: isDarkMode ? Colors.white : Colors.black,
          },
        ]}>
        {title}
      </Text>
      <Text
        style={[
          styles.sectionDescription,
          {
            color: isDarkMode ? Colors.light : Colors.dark,
          },
        ]}>
        {children}
      </Text>
    </View>
  );
};

function setImageBlob(lonNum, latNum) {
  const lon = (lonNum / 10000).toString();
  const lat = (latNum / 10000).toString();
  console.log(lon, lat);
  return fetch(`https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/${lon},${lat},19,0,0/1200x600/?access_token=${ACCESS_TOKEN}`, {
    method: 'GET',
    redirect: 'follow',
  }).then((response) => {
    return response.blob();
  }).then((response) => {
    return URL.createObjectURL(response);
  })

}

function renderItem({ item }) {
  let imageUri = "data:image/png;base64," + item;
  console.log(imageUri);
  return <Image source={{uri: item}} style={{ height: 100 }} />
}

const imageArray = new Array(11).fill().map((_, i) => setImageBlob(lon+(i*10), lat, ));

const App: () => Node = () => {
  const isDarkMode = useColorScheme() === 'dark';

  //const [images, setImages] = useState([]);
  const [image, setImage] = useState<string>('');
  const [images, setImages] = useState<Array<string>>([]);

  const getData = async () => {
    fetch(`https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/${randomLongitude},${randomLatitude},4,0,0/1200x600/?access_token=${ACCESS_TOKEN}`, {
      method: 'GET',
      redirect: 'follow',
    }).then((response) => {
      return response.blob();
    }).then((response) => {
      setImage(URL.createObjectURL(response));
    }).catch((err) => console.error(err));  
  }



  const backgroundStyle = {
    backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,
  };

  useEffect(() => {
    getData();
    Promise.all(imageArray).then(results => {
      console.log("type", typeof(results));
      setImages(results)
    });
}, []);

  return (
    <SafeAreaView style={backgroundStyle}>
      <StatusBar barStyle={isDarkMode ? 'light-content' : 'dark-content'} />
      <FlatList data={images} renderItem={renderItem} />
      <ScrollView
        contentInsetAdjustmentBehavior="automatic"
        style={backgroundStyle}>
        <Header />
        <View
          style={{
            backgroundColor: isDarkMode ? Colors.black : Colors.white,
          }}>
          <Image source={{uri: image}} style={{width: 200, height: 200}} />
          <Section title="Step One">
            Edit <Text style={styles.highlight}>App.js</Text> to change this
            screen and then come back to see your edits.
          </Section>
          <Section title="See Your Changes">
            <ReloadInstructions />
          </Section>
          <Section title="Debug">
            <DebugInstructions />
          </Section>
          <Section title="Learn More">
            Read the docs to discover what to do next:
          </Section>
          <LearnMoreLinks />
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  sectionContainer: {
    marginTop: 32,
    paddingHorizontal: 24,
  },
  sectionTitle: {
    fontSize: 24,
    fontWeight: '600',
  },
  sectionDescription: {
    marginTop: 8,
    fontSize: 18,
    fontWeight: '400',
  },
  highlight: {
    fontWeight: '700',
  },
});

export default App;
