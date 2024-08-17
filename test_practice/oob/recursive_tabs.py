def getActiveTab(tabs, active_route):
    def recursiveTab(curr_tab_state, curr_route):
        if curr_route == active_route:
            return curr_tab_state
        if not curr_tab_state["children"] or not len(curr_tab_state["children"]):
            return None
        for children in curr_tab_state["children"]:
            active_tab = recursiveTab(children, curr_route + "/" + children["viewModel"]["url"])
            if active_tab is None:
                continue
            return active_tab
        return None

    curr_level = tabs["viewModel"]["url"]
    return recursiveTab(tabs, curr_level)


if __name__ == '__main__':
    _tabs = {
        "viewModel": {
            "url": "/main",
            "key": "main_",
            "closable": True,
            "name": "Dashboard",
            "iconName": "946b23a9-8e9c-4649-9b40-098b59822e9a",
            "routerQueryParams": {
                "projectId": "ca484da3-de1c-31fa-b7d4-82b2f12bd37d",
                "activityId": "231b6561-6f3b-4238-a0de-b9866237c5da"
            },
            "active": True,
            "customRoute": None
        },
        "children": [
            {
                "viewModel": {
                    "url": "/pm",
                    "key": "main_pm_",
                    "closable": True,
                    "name": "Project Management",
                    "iconName": "946b23a9-8e9c-4649-9b40-098b59822e9a",
                    "active": False,
                    "customRoute": None,
                    "routerQueryParams": {}
                },
                "children": [
                    {
                        "viewModel": {
                            "url": "/dashboard",
                            "key": "dashboard_activityId_df7a3874-4bab-4210-a1f2-dcd3648dbb61_",
                            "closable": True,
                            "name": "Dashboard",
                            "iconName": "946b23a9-8e9c-4649-9b40-098b59822e9a",
                            "active": False,
                            "routerQueryParams": {
                                "activityId": "df7a3874-4bab-4210-a1f2-dcd3648dbb61"
                            }
                        },
                        "children": [],
                        "routerParams": {
                            "routePart": "dashboard",
                            "queryParams": {
                                "activityId": "df7a3874-4bab-4210-a1f2-dcd3648dbb61"
                            }
                        }
                    },
                    {
                        "viewModel": {
                            "url": "/dashboard",
                            "active": True,
                            "key": "main_pm_dashboard_",
                            "routerQueryParams": {}
                        },
                        "children": [],
                        "routerParams": {
                            "routePart": "dashboard",
                            "queryParams": {}
                        }
                    },
                    {
                        "viewModel": {
                            "url": "/projects",
                            "active": False,
                            "key": "projects_activityId_df7a3874-4bab-4210-a1f2-dcd3648dbb61_",
                            "routerQueryParams": {
                                "activityId": "df7a3874-4bab-4210-a1f2-dcd3648dbb61"
                            }
                        },
                        "children": [],
                        "routerParams": {
                            "routePart": "projects",
                            "queryParams": {
                                "activityId": "df7a3874-4bab-4210-a1f2-dcd3648dbb61"
                            }
                        }
                    },
                    {
                        "viewModel": {
                            "url": "/activities",
                            "active": False,
                            "key": "activities_",
                            "routerQueryParams": {
                                "activityId": "df7a3874-4bab-4210-a1f2-dcd3648dbb61"
                            }
                        },
                        "children": [],
                        "routerParams": {
                            "routePart": "activities",
                            "queryParams": {
                                "activityId": "df7a3874-4bab-4210-a1f2-dcd3648dbb61"
                            }
                        }
                    }
                ],
                "routerParams": {
                    "routePart": "pm",
                    "queryParams": {}
                }
            },
            {
                "viewModel": {
                    "url": "/pm/projects/project",
                    "key": "main_pm_projects_project_projectId_ca484da3-de1c-31fa-b7d4-82b2f12bd37d_",
                    "closable": True,
                    "name": "Project",
                    "iconName": "946b23a9-8e9c-4649-9b40-098b59822e9a",
                    "routerQueryParams": {
                        "projectId": "ca484da3-de1c-31fa-b7d4-82b2f12bd37d",
                        "activityId": "231b6561-6f3b-4238-a0de-b9866237c5da"
                    },
                    "active": True,
                    "customRoute": None
                },
                "children": [
                    {
                        "viewModel": {
                            "url": "/details",
                            "key": "main_pm_projects_project_details_projectId_ca484da3-de1c-31fa-b7d4-82b2f12bd37d_",
                            "closable": True,
                            "name": "Details",
                            "iconName": "946b23a9-8e9c-4649-9b40-098b59822e9a",
                            "routerQueryParams": {
                                "projectId": "ca484da3-de1c-31fa-b7d4-82b2f12bd37d"
                            },
                            "active": False,
                            "customData": {}
                        },
                        "children": [],
                        "routerParams": {
                            "routePart": "details",
                            "queryParams": {
                                "projectId": "ca484da3-de1c-31fa-b7d4-82b2f12bd37d"
                            }
                        }
                    },
                    {
                        "viewModel": {
                            "url": "/activities",
                            "active": True,
                            "key": "main_pm_projects_project_activities_",
                            "routerQueryParams": {
                                "projectId": "ca484da3-de1c-31fa-b7d4-82b2f12bd37d"
                            }
                        },
                        "children": [],
                        "routerParams": {
                            "routePart": "activities",
                            "queryParams": {
                                "projectId": "ca484da3-de1c-31fa-b7d4-82b2f12bd37d"
                            }
                        }
                    }
                ],
                "routerParams": {
                    "routePart": "pm/projects/project",
                    "queryParams": {
                        "projectId": "ca484da3-de1c-31fa-b7d4-82b2f12bd37d"
                    }
                }
            }
        ],
        "routerParams": {
            "routePart": "main",
            "queryParams": {}
        }
    }
    curr_activated_route = 'main/pm/projects/project/activities'
    active_tab = getActiveTab(_tabs, curr_activated_route)
    print(active_tab["routerParams"]["routePart"])
