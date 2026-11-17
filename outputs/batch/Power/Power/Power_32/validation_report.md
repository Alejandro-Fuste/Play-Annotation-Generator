# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_32`
- **Input XML**: `outputs/batch/Power/Power/Power_32/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [29-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [124-128] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-190] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-197] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-249] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-160] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-177] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-189] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-152] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-204] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [124-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-165] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-229] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-143] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-191] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-112] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-168] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-123] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-66] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-128] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-140] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-148] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-190] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-157] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-256] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-160] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-206] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-222] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-235] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-241] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-260] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-264] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-241] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-206] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-225] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-228] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-253] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-231] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-267] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-253] for track '32' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.