# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Power_4`
- **Input XML**: `output_showcase_final/Power/Power_4/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_PullBlock' at frame 129 targets track ID '183', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 9: Duplicate assignment for track ID 'NV' in grid. Overwriting previous assignment.
> - Row 9: Duplicate assignment for track ID 'NV' in grid. Overwriting previous assignment.
> - Row 10: Duplicate assignment for track ID 'NV' in grid. Overwriting previous assignment.
> - Row 10: Duplicate assignment for track ID 'NV' in grid. Overwriting previous assignment.
> - Row 10: Duplicate assignment for track ID 'NV' in grid. Overwriting previous assignment.
> - Invalid track ID 'NV' in Player Track ID sheet. Must be an integer.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '0' (OLB) duration 283 frames exceeds threshold 90 frames [start=17, end=299].
> - Validation warning: Action 'Action_PullBlock' for track '5' (LG) duration 171 frames exceeds threshold 90 frames [start=129, end=299].
> - Validation warning: Action 'Action_DownBlock' for track '9' (RT) duration 283 frames exceeds threshold 90 frames [start=17, end=299].
> - Action 'Action_PreSnap' range [6-143] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-182] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-187] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-184] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [129-147] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [149-171] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [190-226] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-209] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-204] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-220] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [17-152] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-130] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-143] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-158] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-208] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-227] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-33] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-66] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-200] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-202] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-164] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-209] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-184] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-205] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-216] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-255] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.