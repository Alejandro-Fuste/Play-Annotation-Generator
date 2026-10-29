# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Duo_42`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_42/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 20 |
| Ball Tracks | 2 |
| CSV events parsed | 15 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 268 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_ComboBlock' at frame 175 targets track ID '24', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
> - Action 'Action_PreSnap' range [0-268] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-244] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [175-193] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-206] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-220] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-268] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-229] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-260] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-268] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-253] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-240] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-208] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-218] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-195] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-237] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-244] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-248] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-268] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-259] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-203] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-260] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-92] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-256] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-8] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-62] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-164] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-246] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-268] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-260] for track '21' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.