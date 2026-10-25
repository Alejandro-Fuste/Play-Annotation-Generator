# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_112`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_112/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_BallSnap' at frame 77 targets track ID '?', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_RunBlock' for track '19' has invalid range: start=49, end=35. Clamping end to start.
> - Action 'Action_SecureCatch' range [108-122] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-157] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [49-120] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [122-123] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [49-152] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [49-158] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-91] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-287] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-290] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-260] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [49-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-149] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-231] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-118] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-35] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-170] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-48] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-53] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-153] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-68] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-148] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-155] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-217] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-231] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-140] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-157] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-262] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-290] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-263] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-285] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-285] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.