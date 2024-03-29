import React, { FC, useState } from 'react';
import MapboxGL from '@rnmapbox/maps';
import { Button, StyleSheet, Text } from 'react-native';

import sheet from '../../styles/sheet';
import Page from '../common/Page';
import Bubble from '../common/Bubble';

enum OrnamentType {
  Logo = 'logo',
  Attribution = 'attribution',
  Compass = 'compass',
  ScaleBar = 'scaleBar',
}

enum OrnamentPosition {
  TopLeft = 'topLeft',
  TopRight = 'topRight',
  BottomRight = 'bottomRight',
  BottomLeft = 'bottomLeft',
}

const POSITIONS = {
  [OrnamentPosition.TopLeft]: { top: 8, left: 8 },
  [OrnamentPosition.TopRight]: { top: 8, right: 8 },
  [OrnamentPosition.BottomRight]: { bottom: 8, right: 8 },
  [OrnamentPosition.BottomLeft]: { bottom: 8, left: 8 },
};

const styles = StyleSheet.create({
  bubble: {
    marginBottom: 96,
  },
});

type OrnamentButtonsProps = {
  ornamentType: OrnamentType;
  visibility: Record<OrnamentType, true | false | undefined>;
  position: Record<OrnamentType, OrnamentPosition>;
  onPressVisibility: (ornamentType: OrnamentType) => void;
  onPressPosition: (ornamentType: OrnamentType) => void;
};

const OrnamentButtons: FC<OrnamentButtonsProps> = ({
  ornamentType,
  visibility,
  position,
  onPressVisibility,
  onPressPosition,
}) => (
  <>
    <Button
      title={'Visiblity: ' + visibility[ornamentType]}
      onPress={(): void => onPressVisibility(ornamentType)}
    />
    <Button
      title={'Position: ' + position[ornamentType]}
      onPress={(): void => onPressPosition(ornamentType)}
    />
  </>
);

const ShowMap: FC<any> = (props) => {
  const [visibility, setVisibility] = useState({
    [OrnamentType.Logo]: undefined,
    [OrnamentType.Attribution]: undefined,
    [OrnamentType.Compass]: undefined,
    [OrnamentType.ScaleBar]: undefined,
  });

  const [position, setPosition] = useState({
    [OrnamentType.Logo]: OrnamentPosition.BottomLeft,
    [OrnamentType.Attribution]: OrnamentPosition.BottomRight,
    [OrnamentType.Compass]: OrnamentPosition.TopRight,
    [OrnamentType.ScaleBar]: OrnamentPosition.TopLeft,
  });

  const handlePressVisibility = (ornamentType: OrnamentType): void => {
    setVisibility((prevState) => {
      let newValue;

      if (prevState[ornamentType] === undefined) {
        newValue = true;
      } else if (prevState[ornamentType] === true) {
        newValue = false;
      } else if (prevState[ornamentType] === false) {
        newValue = undefined;
      }

      return { ...prevState, [ornamentType]: newValue };
    });
  };

  const handlePressPosition = (ornamentType: OrnamentType): void => {
    setPosition((prevState) => {
      let newValue;

      if (prevState[ornamentType] === OrnamentPosition.TopLeft) {
        newValue = OrnamentPosition.TopRight;
      } else if (prevState[ornamentType] === OrnamentPosition.TopRight) {
        newValue = OrnamentPosition.BottomRight;
      } else if (prevState[ornamentType] === OrnamentPosition.BottomRight) {
        newValue = OrnamentPosition.BottomLeft;
      } else if (prevState[ornamentType] === OrnamentPosition.BottomLeft) {
        newValue = OrnamentPosition.TopLeft;
      }

      return { ...prevState, [ornamentType]: newValue };
    });
  };

  return (
    <Page {...props}>
      <MapboxGL.MapView
        style={sheet.matchParent}
        logoEnabled={visibility[OrnamentType.Logo]}
        logoPosition={POSITIONS[position[OrnamentType.Logo]]}
        attributionEnabled={visibility[OrnamentType.Attribution]}
        attributionPosition={POSITIONS[position[OrnamentType.Attribution]]}
        compassEnabled={visibility[OrnamentType.Compass]}
        compassPosition={POSITIONS[position[OrnamentType.Compass]]}
        scaleBarEnabled={visibility[OrnamentType.ScaleBar]}
        scaleBarPosition={POSITIONS[position[OrnamentType.ScaleBar]]}
      >
        <MapboxGL.Camera />
      </MapboxGL.MapView>

      <Bubble style={styles.bubble}>
        <Text>Logo</Text>
        <OrnamentButtons
          ornamentType={OrnamentType.Logo}
          visibility={visibility}
          position={position}
          onPressVisibility={handlePressVisibility}
          onPressPosition={handlePressPosition}
        />

        <Text>Attribution</Text>
        <OrnamentButtons
          ornamentType={OrnamentType.Attribution}
          visibility={visibility}
          position={position}
          onPressVisibility={handlePressVisibility}
          onPressPosition={handlePressPosition}
        />

        <Text>Compass</Text>
        <OrnamentButtons
          ornamentType={OrnamentType.Compass}
          visibility={visibility}
          position={position}
          onPressVisibility={handlePressVisibility}
          onPressPosition={handlePressPosition}
        />

        <Text>ScaleBar</Text>
        <OrnamentButtons
          ornamentType={OrnamentType.ScaleBar}
          visibility={visibility}
          position={position}
          onPressVisibility={handlePressVisibility}
          onPressPosition={handlePressPosition}
        />
      </Bubble>
    </Page>
  );
};

export default ShowMap;
