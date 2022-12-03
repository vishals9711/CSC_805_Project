import { Button, Col, Row, Select, Skeleton } from 'antd';
import React, { useState } from 'react';
import { getCharts } from '../services/cancerAPI';
import { FEATURES } from './constants';
import { Card } from 'antd';
import { Typography } from 'antd';

const { Title } = Typography;

const { Meta } = Card;

const Visualization = (): React.ReactElement => {
  const { Option } = Select;
  const [selectedFeatures, setSelectedFeatures] = useState<string[]>([]);
  const [selectedCharts, setSelectedCharts] = useState<string[]>([]);
  const [responseCharts, setResponseCharts] = useState<{ [key: string]: string } | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  const returnImage = (result: string) => {
    const byteCharacters = atob(result);
    const byteNumbers = new Array(byteCharacters.length);
    for (let i = 0; i < byteCharacters.length; i++) {
      byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    const image = new Blob([new Uint8Array(byteNumbers)], { type: 'image/png' });
    return URL.createObjectURL(image);
  };

  const getVisualization = async () => {
    setResponseCharts(null);
    setLoading(true);
    await getCharts(selectedFeatures, selectedCharts).then((data) => {
      const imageObj: { [key: string]: string } = {};
      Object.keys(data).forEach((key) => {
        imageObj[key] = returnImage(data[key]);
      });
      setResponseCharts(imageObj);
    });
    setLoading(false);
  };

  const returnImageCard = (data: { title: string; src: string }) => {
    const { src, title } = data;
    return (
      <Card cover={<img alt={title} src={src} />}>
        <Meta title={title} style={{ display: 'flex', margin: 'auto', alignItems: 'center', justifyContent: 'center' }} />
      </Card>
    );
  };

  const checkIfValid = () => !(selectedFeatures.length > 0 && selectedCharts.length > 0);

  return (
    <Row gutter={[16, 16]} justify={'center'}>
      <Col className='gutter-row' span={24}>
        <Select
          mode='multiple'
          allowClear
          style={{ width: '400px' }}
          placeholder='Select Upto 10 Features to Visualize'
          onChange={(value) => {
            setSelectedFeatures([...value]);
            console.log(`selected ${value}`);
          }}
          maxTagCount={10}
          size={'large'}
        >
          {FEATURES.sort().map((data, index) => (
            <Option
              key={index.toString(36) + index}
              disabled={selectedFeatures.length > 9 ? (selectedFeatures.includes(data.key) ? false : true) : false}
              value={data.key}
            >
              {data.label}
            </Option>
          ))}
        </Select>
      </Col>
      <Col span={24}>
        <Title level={5}>* For Joint Plot, only first 2 features will be selected.</Title>
      </Col>

      <Col className='gutter-row' span={24}>
        <Select
          size={'large'}
          mode='multiple'
          allowClear
          style={{ width: '400px', marginTop: '10rem' }}
          placeholder='Select Upto 2 Chart Types to Visualize'
          onChange={(value) => setSelectedCharts([...value])}
          maxTagCount={10}
        >
          {['Violin Plot', 'Box Plot', 'Joint Plot', 'Swarm Plot', 'HeatMap'].map((data, index) => (
            <Option key={index.toString(36) + index} disabled={selectedCharts.length > 1 ? (selectedCharts.includes(data) ? false : true) : false} value={data}>
              {data}
            </Option>
          ))}
        </Select>
      </Col>
      <Col className='gutter-row' span={24} style={{ marginTop: '4rem' }}>
        <Button size={'middle'} onClick={getVisualization} disabled={checkIfValid()}>
          Get Visualization
        </Button>
      </Col>
      <Col className='gutter-row' span={24} style={{ marginTop: '4rem' }}>
        {loading ? (
          <>
            <Row>
              <Col span={8}></Col>
              <Col span={4}>
                <Skeleton.Image active={true} />
              </Col>
              <Col span={4}>
                <Skeleton.Image active={true} />
              </Col>
              <Col span={8}></Col>
            </Row>
          </>
        ) : (
          <Row gutter={[8, 8]}>
            <Col span={2}></Col>
            {responseCharts &&
              Object.keys(responseCharts).map((key, index) => {
                return (
                  <Col className='gutter-row' span={10} key={`${index}_card`}>
                    {returnImageCard({ title: key, src: responseCharts[key] })}
                  </Col>
                );
              })}
            <Col span={2}></Col>
          </Row>
        )}
      </Col>
    </Row>
  );
};

export default Visualization;
