# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_154`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_154/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 123 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '0' (WR1) duration 100 frames exceeds threshold 90 frames [start=294, end=393].
> - Validation warning: Action 'Action_DownBlock' for track '12' (DE2) duration 100 frames exceeds threshold 90 frames [start=294, end=393].
> - Action 'Action_DownBlock' range [294-346] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [294-315] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [338-343] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [336-563] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [294-332] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-342] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-353] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [418-420] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-319] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-332] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-341] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-367] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-394] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-350] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-359] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-291] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [294-311] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [394-556] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [294-318] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [321-336] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [347-353] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [358-367] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-147] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-180] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-219] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-22] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-44] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-54] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-98] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-476] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-482] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [484-564] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-184] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-376] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-310] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-324] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-333] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-338] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-344] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-413] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-326] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-348] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [359-361] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-569] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-377] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [382-526] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-381] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-439] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-461] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [463-466] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-473] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-477] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-488] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-538] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [552-553] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [555-556] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [564-568] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-404] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-416] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-441] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-435] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-539] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-445] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-390] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-480] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-447] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [464-466] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-472] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-512] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-529] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [532-533] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-541] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [543-544] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-553] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-537] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-540] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [546-547] for track '38' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.