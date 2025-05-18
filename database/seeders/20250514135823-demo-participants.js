'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.bulkInsert('participants', [
      {
        id: '44444444-4444-4444-4444-444444444444',
        meeting_id: '33333333-3333-3333-3333-333333333333',
        user_id: '22222222-2222-2222-2222-222222222222',
        email: 'dev@example.com',
        created_at: new Date(),
        updated_at: new Date()
      }
    ]);
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.bulkDelete('participants', null, {});
  }
};

