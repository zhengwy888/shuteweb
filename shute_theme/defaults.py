from mezzanine.conf import register_setting

register_setting(
        name="ADMIN_MENU_ORDER",
        description="Controls the ordering and grouping of the admin menu.",
        editable=False,
        default = ( ("Content", ("pages.Page", "blog.BlogPost",
                "generic.ThreadedComment", "blog.BlogCategory",
                ("Media Library", "fb_browse"),)),
             ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
             ("Users", ("auth.User","auth.Group",)),
            ),
        )
