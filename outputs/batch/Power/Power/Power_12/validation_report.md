# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_12`
- **Input XML**: `outputs/batch/Power/Power/Power_12/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [15-177] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-183] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-187] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-152] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-112] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-239] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-194] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-212] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-219] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-226] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [120-135] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-187] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-200] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-145] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [120-127] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-221] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-215] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-230] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-170] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-145] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-153] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-182] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-135] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-119] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [120-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-188] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-79] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-112] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-213] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-131] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-132] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-151] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-184] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-214] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-228] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-222] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-232] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-217] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-239] for track '23' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.