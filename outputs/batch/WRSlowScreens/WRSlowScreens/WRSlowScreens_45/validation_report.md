# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `WRSlowScreens_45`
- **Input XML**: `outputs/batch/WRSlowScreens/WRSlowScreens/WRSlowScreens_45/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/WRSlowScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [18–34], lower_priority='Action_PassBlock' annotated_start=21, effective_Action_PassBlock_start=35.
> - Action 'Action_None' range [18-206] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-233] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-124] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-170] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-177] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-168] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-112] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-121] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-236] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-73] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-152] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-237] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [18-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-214] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-46] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-193] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-69] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-237] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-148] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-205] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-95] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [98-102] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [105-225] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-213] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-39] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-50] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [18-30] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [39-66] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [55-132] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-218] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-93] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-106] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-230] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-128] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-124] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-213] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-218] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-232] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-228] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-239] for track '30' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.