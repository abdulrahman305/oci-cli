# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.ai_document import AIServiceDocumentClient

MODULE_TO_TYPE_MAPPINGS["ai_document"] = oci.ai_document.models.ai_document_type_mapping
if CLIENT_MAP.get("ai_document") is None:
    CLIENT_MAP["ai_document"] = {}
CLIENT_MAP["ai_document"]["ai_service_document"] = AIServiceDocumentClient
