# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_182`
- **Input XML**: `outputs/batch/Power/Power/Power_182/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [8-123] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-190] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-181] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [123-152] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-118] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-249] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-251] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-254] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-257] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-267] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [123-129] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-259] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-199] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-23] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-126] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-132] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-154] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-207] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-216] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-223] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-184] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-173] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-266] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-207] for track '25' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.