#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
import os
import json
import logging
import boto3

import DbAccessByPymySQL

def lambda_handler(event, context):

    # 環境変数にパラメータストアに登録する変数名を定義
    # 環境変数に定義した変数名などを一括取得
    # パラメータストアから情報取得
    
    db_endpoint_key = os.environ['db_endpoint']
    db_user_key = os.environ['db_user']
    db_passwd_key = os.environ['db_passwd']
    db_schema_key = os.environ['db_schema']
    region = os.environ['region']
    sql = os.environ['sql']

    __get_params([db_endpoint_key,db_user_key,db_passwd_key,db_schema_key])


    # DBアクセスを実施
    dbaccess = DbAccessByPymySQL(endpoint, db_user, db_passwd, db_schema, 'utf8')
    result = dbaccess.select_all(sql)
    dbaccess.close()
    
    # 結果を処理
    logging.debug(result)    

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


def __get_params(param_keys):
    ssm = boto3.client('ssm',region_name = 'ap-northeasr-1')
    response = ssm.get_parameters(
        
        Names=param_keys,
        WithDecryption=True
    )
    return response


def __extract_ssm_param_values(response_from_ssm,param_keys):
    param_dict = {}
    for item in response_from_ssm:
        param_dict[item['Parameter']['Name']] = item['Parameter']['Value']
    
    # TODO param_keysの利用
    
    return param_dict



