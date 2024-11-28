# coding=utf-8
from django.contrib.admin import site
from django.contrib.contenttypes.models import ContentType
from django.db import connection
from django.http.response import HttpResponseRedirect
from django.utils.encoding import force_str
from django.template.response import TemplateResponse
from django.contrib import messages
from django.contrib.auth.models import User
from invent.models import StockIn,StockOut,InitialInventory,WareReturn,WareAdjust
from django.utils.translation import gettext_lazy as _


def action_in(request,object_id):
    """
    Warehouse Operation
    :param request:
    :param object_id:
    :return:
    """
    title = _("Are you sure?")
    obj = StockIn.objects.get(id=int(object_id))
    opts = obj._meta
    objects_name = force_str(opts.verbose_name)

    if request.POST.get("post"):
        try:
            obj.action_entry(request)
            messages.success(request,_('check in successfully'))
        except Exception as e:
            messages.error(request,e)

        return HttpResponseRedirect("/admin/invent/stockin/%s"%(object_id))

    context = dict(
        site.each_context(request),
        title=title,
        opts=opts,
        objects_name=objects_name,
        object=obj,
    )
    request.current_app = site.name

    return TemplateResponse(request,'admin/invent/stockin/in_confirmation.html', context)


def action_out(request,object_id):
    """
    Outbound Operation
    :param request:
    :param object_id:
    :return:
    """
    title = _("Are you sure?")
    obj = StockOut.objects.get(id=int(object_id))
    opts = obj._meta
    objects_name = force_str(opts.verbose_name)

    if request.POST.get("post"):
        try:
            obj.action_out(request)
            messages.success(request,_('check out successfully'))
        except Exception as e:
            messages.error(request,e)
        return HttpResponseRedirect("/admin/invent/stockout/%s"%(object_id))

    context = dict(
        site.each_context(request),
        title=title,
        opts=opts,
        objects_name=objects_name,
        object=obj,
    )
    request.current_app = site.name

    return TemplateResponse(request,'admin/invent/stockout/out_confirmation.html', context)


def action_init(request,object_id):
    """
    Initial warehousing operation
    :param request:
    :param object_id:
    :return:
    """
    title = _("Are you sure?")
    obj = InitialInventory.objects.get(id=int(object_id))
    opts = obj._meta
    objects_name = force_str(opts.verbose_name)

    if request.POST.get("post"):
        try:
            obj.init_entry(request)
            messages.success(request,_('check in successfully'))
        except Exception as e:
            messages.error(request,e)

        return HttpResponseRedirect("/admin/invent/initialinventory/%s"%(object_id))

    context = dict(
        site.each_context(request),
        title=title,
        opts=opts,
        objects_name=objects_name,
        object=obj,
    )
    request.current_app = site.name

    return TemplateResponse(request,'admin/invent/stockin/in_confirmation.html', context)


def action_return(request,object_id):
    """
    Return to warehouse
    :param request:
    :param object_id:
    :return:
    """
    title = _("Are you sure?")
    obj = WareReturn.objects.get(id=int(object_id))
    opts = obj._meta
    objects_name = force_str(opts.verbose_name)

    if request.POST.get("post"):
        try:
            obj.action_return(request)
            messages.success(request,_('check in successfully'))
        except Exception as e:
            messages.error(request,e)

        return HttpResponseRedirect("/admin/invent/warereturn/%s"%(object_id))

    context = dict(
        site.each_context(request),
        title=title,
        opts=opts,
        objects_name=objects_name,
        object=obj,
    )
    request.current_app = site.name

    return TemplateResponse(request,'admin/invent/stockin/in_confirmation.html', context)


def action_adjust(request,object_id):
    """
    Adjustment Operation
    :param request:
    :param object_id:
    :return:
    """
    title = _("Are you sure?")
    obj = WareAdjust.objects.get(id=int(object_id))
    opts = obj._meta
    objects_name = force_str(opts.verbose_name)

    if request.POST.get("post"):
        try:
            obj.action_adjust(request)
            messages.success(request,_('check in successfully'))
        except Exception as e:
            messages.error(request,e)

        return HttpResponseRedirect("/admin/invent/wareadjust/%s"%(object_id))

    context = dict(
        site.each_context(request),
        title=title,
        opts=opts,
        objects_name=objects_name,
        object=obj,
    )
    request.current_app = site.name

    return TemplateResponse(request,'admin/invent/stockin/in_confirmation.html', context)