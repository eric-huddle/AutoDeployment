SUIT_CONFIG = {
    'ADMIN_NAME': 'Huddle',
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,
    'LIST_PER_PAGE': 100,
    'MENU': (
        'sites',
        {
          'label': 'Customers',
          'icon': 'icon-user',
          'models': (
              'users.customer',
              'users.address',
              'notes.usernote',
          )
        },
        {
          'label': 'Car Insurance',
          'icon': 'icon-road',
          'models': (
            {'model': 'policies.carpolicy', 'label': 'Policies'},
            {'model': 'quotes.carquote', 'label': 'Quotes'},
            {'model': 'claims.claim', 'label': 'Claims'},
            {'model': 'pds.carpds', 'label': 'PDS'},
          )
        },
        {
          'label': 'Travel Insurance',
          'icon': 'icon-plane',
          'models': (
            {'model': 'policies.travelpolicy', 'label': 'Policies'},
            {'model': 'quotes.travelquote', 'label': 'Quotes'},
            {'model': 'claims.claim', 'label': 'Claims'},
            {'model': 'policies.travelreport', 'label': 'Report'},
            {'model': 'pds.travelpds', 'label': 'PDS'},
          )
        },
        {
          'label': 'Home Insurance',
          'icon': 'icon-home',
          'models': (
            {'url': '/', 'label': 'Quotes'},
            {'url': '/', 'label': 'Policies'},
            {'url': '/', 'label': 'Claims'},
          )
        },
        {
          'label': 'P2P Lending',
          'icon': 'icon-briefcase',
          'models': (
            {'url': '/', 'label': 'Borrowing'},
            {'url': '/', 'label': 'Lending'},
          )
        },
        {
          'label': 'Rewards',
          'icon': 'icon-gift',
          'models': (
            {'model': 'discounts.discount', 'label': 'Discounts'},
            {'model': 'points.points', 'label': 'Earning'},
            {'url': '/', 'label': 'Currency'},
            {'url': '/', 'label': 'Redemption'},
            {'url': '/', 'label': 'Balance Sheet'},
          )
        },
        {
          'label': 'Money Manager',
          'icon': 'icon-leaf',
          'models': (
            {'url': '/', 'label': 'Credit Score'},
            {'url': '/', 'label': 'Insurance Checkup'},
            {'url': '/', 'label': 'Credit Card Challenge'},
            {'url': '/', 'label': 'Q&A'},
          )
        },
        {
          'label': 'Q & A\'s',
          'icon': 'icon-comment',
          'models': (
            'qanda.question',
            'qanda.questionview',
            'qanda.questionlike',
            'qanda.answer',
            'qanda.answervote',
            'qanda.topic',
          )
        },

        {
          'label': 'Content',
          'icon': 'icon-list-alt',
          'models': (
            'news.smallcampaign',
            'news.campaign',
            'news.video',
            'news.article',
          )
        },
        {
          'label': 'Geodata',
          'icon': 'icon-globe',
          'models': (
            'geography.country',
            'geography.suburb',
          )
        },
        {
          'label': 'System',
          'icon': 'icon-cog',
          'models': (
            'huddles.huddle',
            'alerts.alert',
            'notifications.notification',
            'users.staff',
            'auth.group',
          )
        }
    )
}
