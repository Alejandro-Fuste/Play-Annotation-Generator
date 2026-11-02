# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `WRSlowScreens_2`
- **Input XML**: `outputs/batch/WRSlowScreens/WRSlowScreens/WRSlowScreens_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/WRSlowScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [8–25], lower_priority='Action_PassBlock' annotated_start=11, effective_Action_PassBlock_start=26.
> - Action 'Action_None' range [8-95] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-156] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-79] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-87] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [141-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-66] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-86] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ReleaseToScreen' range [36-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-87] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-91] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-134] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-163] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-182] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-112] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-92] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-37] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-51] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-7] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-26] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-32] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-54] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [81-231] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-91] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-110] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-215] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-226] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-152] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-146] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-160] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-165] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-187] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-194] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-231] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-214] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-230] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-211] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-223] for track '32' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.