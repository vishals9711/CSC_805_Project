import React from 'react';
import { Route, Routes, useNavigate } from 'react-router-dom';
import './App.css';
import { Layout, Menu } from 'antd';
import Prediction from './Components/Prediction';
import Visualization from './Components/Visualization';
const App = (): React.ReactElement => {
  const { Header, Footer, Content } = Layout;
  const navigate = useNavigate();

  return (
    <Layout>
      <Header style={{ position: 'fixed', zIndex: 1, width: '100%', display: 'flex' }}>
        <Menu
          style={{ margin: 'auto' }}
          theme='dark'
          mode='horizontal'
          defaultSelectedKeys={['/']}
          selectedKeys={[window.location.pathname]}
          onClick={(e) => navigate(e.key)}
        >
          {[
            {
              label: 'Visualize',
              to: '/',
            },
            {
              label: 'Get Prediction',
              to: '/prediction',
            },
          ].map((data) => (
            <Menu.Item key={data.to}>{data.label}</Menu.Item>
          ))}
        </Menu>
      </Header>
      <Content className='app-content'>
        <Routes>
          <Route path='/' element={<Visualization />} />
          <Route path='/prediction' element={<Prediction />} />
        </Routes>
      </Content>
      <Footer>Breast Cancer Prediction ©2022 Created by Darshil &amp; Vishal</Footer>
    </Layout>
  );
};

export default App;
