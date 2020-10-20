class Resource:
    resource='/rest/api/2/search'

    def get_attachment_id(self,*lst_jira):
        for each_jira in range(len(lst_jira)):
            out = ('/rest/api/2/issue/' + each_jira)
            return out



    #print(link_generator('RES-14'))
    #attachment='/rest/api/2/issue/RES-13'
    attachment_metadata='/rest/api/3/attachment/attachment_id'


