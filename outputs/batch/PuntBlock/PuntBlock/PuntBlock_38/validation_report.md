# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_38`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 114 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [27-106] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-173] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-245] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [27-65] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-222] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [223-234] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-60] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-228] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [77-91] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [106-269] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-88] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-202] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-112] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-233] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-61] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-265] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-105] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-206] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-236] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-245] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-267] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-269] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-122] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-118] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-172] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-222] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-69] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-40] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-92] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-248] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [75-153] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-230] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-96] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-121] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-103] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-134] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [137-143] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-157] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-193] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-135] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-155] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-162] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-219] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-206] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-236] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-245] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-171] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '31' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.