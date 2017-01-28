
-XSS
----
public function get_error_name()
{
    // リクエストパラメータを取得
    $param = $this->get_get();
    // リクエストパラメータに名前がセットされている場合
    if (isset($param[parent::NAME])) {
        return $param[parent::NAME];
    // リクエストパラメータに名前がセットされていない場合
    } else {
        return "";
    }
}

----

public function get_error_name()
{
    // リクエストパラメータを取得
    $param = $this->get_get();
    // リクエストパラメータに名前がセットされている場合
    if (isset($param[parent::NAME])) {
        return htmlspecialchars($param[parent::NAME], ENT_QUOTES, "UTF-8");
    // リクエストパラメータに名前がセットされていない場合
    } else {
        return "";
    }
}
